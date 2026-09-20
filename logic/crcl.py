def cal_clcr_results(age, weight, scr, unit_type):
    """
    Logic for the calculation. 
    unit_type: 0 for mg/dL (or mg/mL), 1 for µmol/L
    """
    try:
        # Convert inputs to floats
        age = int(age)
        weight = float(weight)
        scr = float(scr)

        if scr <= 0 or age <= 0 or weight <= 0:
            return None, None
        
        # Step 1: Normalize SCr to mg/dL
        # If user provides µmol/L, divide by 88.4
        # If user provides mg/mL, multiply by 100 (10 mg/mL = 1000 mg/dL)
        if "µmol" in unit_type or "umol" in unit_type:
            scr_mg_dl = scr / 88.4
        elif unit_type == "mg/mL":
            scr_mg_dl = scr * 100
        else:
            scr_mg_dl = scr  # Assume mg/dL

        # Step 2: Cockcroft-Gault Formula
        male_val = ((140 - age) * weight) / (72 * scr_mg_dl)
        female_val = male_val * 0.85
        
        return round(male_val, 2), round(female_val, 2)
        
    except (ValueError, ZeroDivisionError):
        return None, None

def cal_ckd_epi_2009_results(age, scr, unit_type, is_black=False):
    """Logic for the CKD-EPI (2009) eGFR calculation.

    unit_type: "mg/dL", "mg/mL", "µmol/L" (or "umol/L")
    is_black: True to apply Black race modifier (1.159), False otherwise
    Returns: tuple (male_eGFR, female_eGFR) rounded to 2 decimal places, or
    (None, None) on error.
    """
    try:
        # Convert inputs
        age = int(age)
        scr = float(scr)
        unit_type = str(unit_type)

        if scr <= 0 or age <= 0:
            return None, None

        # Step 1: Normalize SCr to mg/dL
        # If user provides µmol/L, divide by 88.4
        # If user provides mg/mL, multiply by 100
        if "µmol" in unit_type or "umol" in unit_type:
            scr_mg_dl = scr / 88.4
        elif unit_type == "mg/mL":
            scr_mg_dl = scr * 100
        else:
            scr_mg_dl = scr  # Assume mg/dL

        # Step 2: Shared factors
        race_factor = 1.159 if is_black else 1.0
        age_factor = 0.993**age

        # Step 3: Male calculation (kappa = 0.9, alpha = -0.411)
        scr_k_m = scr_mg_dl / 0.9
        male_val = (
            141
            * (min(scr_k_m, 1.0) ** -0.411)
            * (max(scr_k_m, 1.0) ** -1.209)
            * age_factor
            * race_factor
        )

        # Step 4: Female calculation (kappa = 0.7, alpha = -0.329, sex modifier = 1.018)
        scr_k_f = scr_mg_dl / 0.7
        female_val = (
            141
            * (min(scr_k_f, 1.0) ** -0.329)
            * (max(scr_k_f, 1.0) ** -1.209)
            * age_factor
            * 1.018
            * race_factor
        )

        return round(male_val, 2), round(female_val, 2)

    except (ValueError, ZeroDivisionError, TypeError):
        return None, None