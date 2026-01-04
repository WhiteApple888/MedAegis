import re
import pandas as pd

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

    return df, final_totals

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
    

def calculate_required_qty(daily_qty, current_balance, duration_days):
    try:
        # Convert inputs to float/int
        daily = float(daily_qty)
        balance = float(current_balance)
        days = int(duration_days)
        
        # Logic: (Needed per day * total days) - what they already have
        return (daily * days) - balance
        
    except (ValueError, TypeError):
        return None