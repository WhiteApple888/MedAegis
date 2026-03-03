import pandas as pd
import re

def parse_medication_data(text):
    rows = []
    current_date = ""
    current_status = ""

    # State management
    line_buffer = []
    fragment_count = 0
    
    # Split text into lines and strip whitespace
    lines = [line.strip() for line in text.strip().split('\n')]

    # Regex to detect date at start of line (e.g., 11-Jan-2026)
    date_pattern = r'(^\d{1,2}-[a-zA-Z]{3}-\d{4}) - (Dispensed|Ordered)'

    # The pattern you provided to validate a "complete" medication line
    valid_line_pattern = r'\t[\d\sa-z]*(?:-\s?){0,1}/[\d\sa-z]*(?:-\s?){0,1}\t'

    for line in lines:
        if not line: continue
        
        header_match = re.match(date_pattern, line)
        if header_match:
            # This is a header line
            current_date = header_match.group(1)
            # Extract status (Ordered or Dispensed)
            current_status = header_match.group(2)
        else:
            # Check if this line is a continuation or a new valid line
            is_valid_structure = re.search(valid_line_pattern, line, re.IGNORECASE)
            if not is_valid_structure:
                fragment_count += 1
                # If count > 0, it means we've found multiple lines of "garbage" or fragments
                line_buffer.append(line)

            else:
                # VALID STRUCTURE FOUND:
                # 1. Join any fragments caught in the buffer to the START of this valid line
                # 2. Reset the count and buffer
                combined_line = " ".join(line_buffer) + " " + line
                line_buffer = []
                fragment_count = 0

                # 3. Only split by \t NOW that the structure is consolidated
                med_details = combined_line.strip().split('\t')
            
                # Ensure we have enough columns (padding if necessary)
                full_row = [current_date, current_status] + med_details
                rows.append(full_row)

    # Create raw DataFrame
    columns = ['Date', 'Status', 'Medication', 'Dosing instructions', 'Date &/or Qty', 'Institution']
    df = pd.DataFrame(rows, columns=columns)
    return df


def quick_clean(text):
    text = str(text).lower().strip()
    text = re.sub(r'\b(?:\d*\.)?\d*(?:mcg|mg|g|ml|tab|tablet|cap|capsule|bottle|btl|drop)s?\b', '', text) # Remove units,
    text = re.sub(r'(?:prefilled-?(?:\s*syringe|pen)|(?:auto(?:-|\s*)?)?(?:injector|injection))s?', '', text) # Remove injection formulation,
    text = re.sub(r'(?:\(|\)|<|>|\\|/|\(cd\)|\(f\))', '', text)  # Remove brand names in brackets and < >, \, /, (cd), (f)
    keywords = [
    'hcl', 'sulfate', 'citrate',  'maleate', 'fumarate', '8s9s', 'kefentech','liptor', 'crestor', 'jardiance',
    'ziagen', 'abilify', 'maintena', 'orencia', 'calquence', 'humira','amgevita', 'differin', 'epiduo', 'epipen','giotrif', 'zaltrap', 'valdoxan', 'alecensa', 'lemtrada', 
    'rapifen', 'myozyme', 'praluent', 'rasilez', 'piqray', 'xanax(?:\s*(?:xr|sr))?', 'caverject', 'mucosolvan', 'gliolan','unasyn', 'kineret', 'eraxis', 'eliquis', 
    'iopidine', 'riamet', 'scemblix', 'erwinase', 'leunase','strattera', '	tecentriq', 'malarone', 'spedra', 'bavencio', 'inlyta', 'azactam', 'sirturo', 'welireg',
    'fasenra', 'narcaricin mite', 'benzac ac', 'difflam(?:\s*forte)??', 'betaserc', 'avastin', 'lumigan(?:\s*pf)?','ganfort(?:\s*pf)?', 'pfree', 'biphozyl',
    'blincyto', 'victrelis', 'tracleer', 'rexulti', 'alunbrig', 'alphagan(?:\s*p)?', 'combigan', 'simbrinza', 'azarga', 'lexotan', 'symbicort', 'duoresp','breztri', 'pulmicort', 
    'cabometyx', 'daivonex', 'enstilar', 'daivobet', 'tegretol', 'leukeran', 'irkevis', 'neoral', 'regpara', 'ciloxan', 'clindoxyl', 'plavix','canesten', 'mycoban', 'zarin', 'zaricort',
    'd-cure', 'codipront', 'procodin', 'hydergine', 'premarin', 'xalkori', 'minims', 'pradaxa', 'tafinlar', 'vizimpro', 'prezista', 'sprycel', 'exjade', 'jadenu', 'ferriprox', 'firmagon',
    'minirin', 'nocdurna', 'pristiq', 'desowen', 'desomedine', 'maxidex', 'dexilant', 'tussils', 'herbesser r', 'tivicay', 'dovato', 'triumeq', 'aricept', 'pifeltro', 'trusopt', 'cosopt-s',
    'dothiepin', 'trulicity', 'cymbalta', 'dupixent', 'revolade', 'descovy', 'truvada', 'clexane', 'lanoxin', 'rozlytrek', 'xtandi', 'myonal', 'eprex', 'recormon', 'balversa', 'erdomed', 
    'aimovig', 'lexapro', 'estramon','oestrogel', 'progynova', 'dicynone', 'enbrel', 'certican', 'repatha', 'lipanthyl supra', 'ferinject', 'tambocor', 'trelegy', 'relvar', 'flixotide',
    'faverin', 'calquence', 'tagrisso', 'forteo', 'lonsurf', 'monurol', 'fucithalmic','reminyl', 'emgality', 'diamicron mr', 'rectogesic', 'simponi', 'zoladex(?:\s*la)?', 'bonviva', 'imbruvica',
    'glivec', 'tanatril', 'remsima', 'maltofer', 'fybogel', 'tibsovo', 'taltz', 'lacipil', 'lamictal', 'forsenol', 'xalatan', 'leqembi', 'xalacom', 'dayvigo', 'harvoni', 'lenvima', 'lucrin depot',
    'leucovorin', 'eligard', 'trajenta(?:\s*duo)?', 'saxenda', 'priadel', 'camcolit', 'lorviqua', 'lotemax', 'cravit', 'latuda', 'celsentri', 'camzyos', 'duspatalin retard', 'circadin', 'alkeran',
    'pentasa', 'salofalk', 'mezavant xl', 'glucophage(?:\s*xr)?', 'concerta', 'medikinet mr', 'ritalin la', 'daktarin', 'gutron', 'betmiga', 'elomet', 'bactroban', 'myfortic', 'abraxane', 'nevanac',
    'rocklatan', 'akynzeo', 'nicotinell(?:\s*tts\s*(?:10|20|30))?', 'nicorette', 'tasigna', 'nimotop', 'ofev', 'octenisan', 'lynparza', 'ryaltris', 'tamiflu', 'isturisa', 'oxynorm', 'oxycontin neo',
    'ibrance', 'invega', 'sustenna', 'creon 10,000', 'seroxat cr', 'votrient', 'fulphila', 'pegasys', 'lyrica', 'stemetil', 'seroquel xr', 'xiffaxan', 'edurant', 'xarelto', 'exelon(?:\s*(5|10))?',
    'requip pd 24 hour', 'neupro', 'inovelon', 'jakavi', 'seretide', 'uptravi', 'xopvio', 'rybelsus', 'ozempic', 'senna', 'renvela', 'mayzent', 'januvia', 'Janumet xr', 'epilim(?: chrono)?', 'lokelma',
    'epclusa', 'vosevi', 'protopic', 'prograf', 'advagaf', 'cialis', 'vyndamax', 'taflotan-s', 'tapcom-s', 'tanakan', 'vemlidy', 'lamisil', 'sondelbay', 'thyrozol', 'nuelin-sr', 'euthyrox', 
    'brilinta', 'spiriva', 'tobrex', 'tobradex', 'xejanz', 'samsca', 'incruse', 'anoro', 'ursofalk', 'co-diovan', 'venclexta', 'vfend', 'marevan', 'zomig(?:\s*rapimelt)?', 'stilnox(?:\s*cr)?',
    ]
    pattern = r'(?:' + '|'.join(keywords) + r')'
    text = re.sub(pattern, '', text)  # Remove salts, brand names and formulations 
    text = re.sub(r'.*(?:monday|tuesday|wednesday|thursday|friday|intervention|delivery|billing|preparation fee).*','', text)  # Remove delivery, intervention and billing lines
    return text.strip()

def get_unique_meds(df):
    # Preprocessing - datetime conversion, sort and quick clean
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce', format='mixed')
    df['medication_lower_case'] = df['Medication'].str.lower().str.strip()
    df_sorted = df.sort_values(by=['Date', 'medication_lower_case'], ascending=[False, True])
    df_sorted['clean_name'] = df['Medication'].apply(quick_clean)

    # Remove empty clean_names and drop duplicates
    df_sorted = df_sorted[df_sorted['clean_name'].str.strip().astype(bool)]
    unique_df = df_sorted.drop_duplicates(subset=['clean_name'], keep='first')
    
    # 3. Merge back with inner join include all rows matching those specific keys
    # We want rows where (Date, clean_name, Status) match the latest_reference to account for separate lines prescriptions.
    keys = ['Date', 'clean_name', 'Status']
    unique_final_df = pd.merge(df_sorted, unique_df[keys], on=keys, how='inner')
    unique_final_df['End Date'] = unique_final_df.apply(calculate_end_date, axis=1)
    unique_final_df = unique_final_df.sort_values(by=['End Date','Date', 'medication_lower_case'], ascending=[False, False, True])
    return unique_final_df.reset_index(drop=True)

def calculate_end_date(row):
    if pd.isna(row['Date']):
        return pd.NaT
    
    # Search for a number followed by a unit (day, week, month)
    # This looks at the 'Date &/or Qty' column first, then 'Dosing instructions'
    text_to_search = f"{row['Date &/or Qty']}".lower().strip()
    
    # Regex pattern: look for digits followed by optional space and a unit
    match = re.search(r'(\d+)\s*(day|week|month|year)s?', text_to_search)
    
    if not match:
        return pd.Timestamp.now()

    quantity = int(match.group(1))
    unit = match.group(2)
    
    # Map units to Pandas DateOffset arguments
    if 'day' in unit:
        return row['Date'] + pd.DateOffset(days=quantity)
    elif 'week' in unit:
        return row['Date'] + pd.DateOffset(weeks=quantity)
    elif 'month' in unit:
        return row['Date'] + pd.DateOffset(months=quantity)
    elif 'year' in unit:
        return row['Date'] + pd.DateOffset(years=quantity) 

def separate_meds_by_frequency(df):
    """
    Splits the DataFrame into Chronic (Regular) and PRN (As Needed) medications.
    """
    # Define keywords for 'as needed' medications
    # \b matches word boundaries; p\.?r\.?n\.? matches prn, p.r.n, or p.r.n.
    prn_pattern = r'when necessary|p\.?r\.?n\.?|when needed|when required'
    
    # Create a mask (True for rows containing PRN keywords)
    is_prn = df['Dosing instructions'].str.contains(prn_pattern, case=False, na=False)
    
    # Split into two dataframes
    df_prn = df[is_prn].copy().reset_index(drop=True)
    df_chronic = df[~is_prn].copy().reset_index(drop=True)
    
    return df_chronic, df_prn

# Execute
def compile_med_list(raw_data):
    df_full = parse_medication_data(raw_data)
    unique_final_df = get_unique_meds(df_full)
    df_chronic, df_prn = separate_meds_by_frequency(unique_final_df)
    return df_chronic, df_prn