import re
import pandas as pd
import numpy as np

# --- 1. EXISTING PARSING LOGIC ---
def process_nehr_data(raw_data):
    """ 
    This function receives the string from the GUI, 
    processes it, and returns the result.
    """

    if not raw_data.strip():
        return "Please provide NEHR Dispensed History."
    
    # 1. Split into individual records based on the Date pattern (DD-Mon-YYYY - Dispensed of D-Mon-YYYY - Dispensed)
    records = re.split(r'\n(?=\d{1,2}-[a-zA-Z]{3}-\d{4} - Dispensed)', raw_data)
    print(records)
    records = [r.strip() for r in records if r.strip()]

    final_data = []

    for record in records:

        try:
            # 1. Extract Date using regex
            pattern1=r'(^\d{1,2}-[a-zA-Z]{3}-\d{4}) - Dispensed'
            date_match = re.search(pattern1, record)
            date = date_match.group(1) if date_match else "N/A"

            # 2. Extract Medication name and formulation using regex
            pattern2 = pattern1 + r'\s+(.*?)(?:tablets?|tabs?|capsules?|caps?)'
            med_match = re.search(pattern2, record, re.DOTALL | re.IGNORECASE).group(2).strip()
            med = med_match if med_match else "Unknown"

            # 3. Find the numerical quantity using regex even if its order with duration is reversed. This ignores '180 days' and picks '360 TAB' even if the order is reversed
            # used re.findall and index from -1 instead of re.search as dosing instruction may use 1 TAB every morning.
            pattern3 = r'(\d+)\s*(tablet|tab|capsule|caps)s?\t(.+)$'
            if qty_form_matches := re.findall(pattern3, record, re.IGNORECASE):
                qty = int(qty_form_matches[-1][0])
                formulation = qty_form_matches[-1][1]
            
            else:
                qty = 0
                formulation = "None"

            # 4. Extract institution using regex
            pattern4 = r'(?:\d*\s[a-z]+\s/\s\d*\s[a-z]+)(.+)$'
            institution_match = re.search(pattern4, record, re.IGNORECASE).group(1).strip()
            institution= institution_match if institution_match else "Unknown"
            final_data.append([date, med, qty, formulation, institution])

        except Exception as e: #for debugging purpose when scraping data
            print(f"Error parsing record: {e}")

    df = pd.DataFrame(final_data, columns=['Date', 'Medication', 'Qty', 'Formulation', 'Institution'])

    
     # 1. Prepare and Sort
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce', format='mixed')
    df = df.dropna(subset=['Date'])
    df = df.sort_values(by='Date')
    #Convert the Data to Dates to remove 00:00:00
    df['Timestamp'] = df['Date'].apply(lambda x: x.timestamp())

    # 2. Normalize the medication column to uppercase for consistency
    df['Medication'] = df['Medication'].str.upper()
    # 3. Calculate cumulative sum grouped by medication
    df["cumulative_sum"] = df.groupby("Medication")["Qty"].cumsum()
    final_totals = df.groupby("Medication")["cumulative_sum"].last()

    print(final_totals.index[0])
    return df, final_totals

# --- 2. EXISTING CALCULATORS ---
def calculate_duration_pd(start_date_str, end_date_str):
    """
    Calculates the number of days between two dates using Pandas.
    """
    try:
        start = pd.to_datetime(start_date_str)
        end = pd.to_datetime(end_date_str)
        
        # Calculate the difference
        duration = (end - start).days
        return duration
    except Exception:
        return f"Invalid"
    
def calculate_end_date_pd(start_date_str, duration_days):
    """
    Calculates the end date based on duration using Pandas.
    """
    try:
        start = pd.to_datetime(start_date_str)
        # Add the duration using Timedelta
        end_date = start + pd.Timedelta(days=int(duration_days))
        
        # Format it back to your preferred NEHR style
        return end_date.strftime('%d-%b-%Y')
    except Exception:
        return None
    
# --- 3. NEW VISUAL TRACKER ENGINE ---
class MedicationEngine:
    """
    This class generates the data for Graph 1 and Graph 2.
    """
    def __init__(self, nehr_df, medication_name, daily_dosage, start_date_str, duration_days):
        # Filter NEHR data for the specific medication
        self.med_df = nehr_df[nehr_df['Medication'] == medication_name.upper()].copy()

        # Setup Parameters
        self.dosage = float(daily_dosage)
        self.start_dt = pd.to_datetime(start_date_str, dayfirst=True)
        self.duration = int(duration_days)
        self.end_dt = self.start_dt + pd.Timedelta(days=self.duration)
        self.report_df = None # To store the results after generation

    def generate_report(self):
        # 1. Create a daily date range
        all_dates = pd.date_range(start=self.start_dt, end=self.end_dt, freq='D')
        df = pd.DataFrame({'Date': all_dates})
        df['Days_Elapsed'] = np.arange(len(df))

        # 2. Perform aggregation to be merged with the daily timeline
        # Group by date in case multiple dispenses happened same day
        agg_rules = {
            'Qty': 'sum',
            'Institution': lambda x: " / ".join(set(x.dropna())),
            'Formulation': lambda x: ", ".join(set(x.dropna())),
            'Medication': 'first' # Since Engine is filtered for one med
            }
        med_daily = self.med_df.groupby('Date').agg(agg_rules).reset_index()

        # 3. Merge the daily timeline with the aggregated data
        # 'left' merge ensures we keep every day in the date_range
        df = pd.merge(df, med_daily, on='Date', how='left')

        # 4. Fill missing values (days where no dispense happened)
        df['Qty'] = df['Qty'].fillna(0)
        df['Institution'] = df['Institution'].fillna("-")
        df['Formulation'] = df['Formulation'].fillna("")

        # 5. Calculate "Running Balance" (The 60 - 30 + 90 Logic)
        # We use a loop or a custom accumulator because daily consumption
        # depends on the balance not dropping below zero
        current_balance = 0
        stock_history = []

        for _, row in df.iterrows():
            # Add what was collected today
            current_balance += row['Qty']
            # Subtract daily dose (cannot go below 0)
            # Note: We subtract AFTER adding today's collection
            current_balance = max(0, current_balance - self.dosage)
            stock_history.append(current_balance)

        df['Patient_Stock'] = stock_history
        df['Timestamp'] = df['Date'].apply(lambda x: x.timestamp())

        # --- GRAPH 1: Target Ceiling ---
        total_needed_at_start = self.duration * self.dosage
        df['Target_Required'] = total_needed_at_start - (df['Days_Elapsed'] * self.dosage)
        df['Target_Required'] = df['Target_Required'].clip(lower=0)
        df['Oversupplied'] = "No"  # Set default
        df.loc[df['Target_Required'] - df['Patient_Stock'] < 0, 'Oversupplied'] = "Yes"

        self.report_df = df # Store it so we don't have to recalculate
        return df
    
    def calculate_supply_gap(self):
        """Calculates quantity needed today to reach the target end date."""
        if self.report_df is None:
            self.generate_report()
        
        today = pd.Timestamp.now().normalize()

        # Filter for today's metrics
        today_row = self.report_df[self.report_df['Date'] == today]
        
        if not today_row.empty:
            current_stock = today_row['Patient_Stock'].values[0]
            target_required = today_row['Target_Required'].values[0]
            # Gap = (What they should have) - (What they actually have)
            gap = max(0, target_required - current_stock)
            return int(np.ceil(gap))
        
        if today < self.start_dt:
            return int(self.duration * self.dosage)
        
        return 0
