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