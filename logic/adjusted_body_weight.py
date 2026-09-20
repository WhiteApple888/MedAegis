def cal_ideal_adj_body_weight(actual_weight_kg : str, height_cm : str) -> tuple[float, float, float, float] | tuple[None, None, None, None]:
    """
    Calculates Ideal Body Weight (IBW) using Devine formula and 
    Adjusted Body Weight (ABW) using a 40% correction factor for both sexes.

    Args:
        actual_weight_kg: Actual body weight in kilograms (as str, float, or int).
        height_cm: Height in centimeters (as str, float, or int).

    Returns:
        tuple: (male_ibw, female_ibw, male_abw, female_abw) rounded to 2 decimals,
               or (None, None, None, None) if inputs are invalid or non-positive.
    """
    # Convert inputs to floats and int
    try:
        actual_weight_kg = float(actual_weight_kg)
        height_cm = float(height_cm)

        if actual_weight_kg <= 0 or height_cm <= 0:
            return (None, None, None, None)

        # Step 1: Calculate IBW
        male_ibw = 50 + 2.3 * (height_cm - 152.4) / 2.54
        female_ibw = 45.5 + 2.3 * (height_cm - 152.4) / 2.54

        # Step 2: Calculate adjBW
        male_abw = male_ibw + 0.4*(actual_weight_kg - male_ibw)
        female_abw = female_ibw + 0.4*(actual_weight_kg - female_ibw)

        return round(male_ibw, 2), round(female_ibw, 2), round(male_abw, 2), round(female_abw, 2)

    except (ValueError, TypeError, ZeroDivisionError):
        return None, None, None, None

def cal_bmi(weight_kg: str, height_cm: str) -> str | None:
    """
    Calculates Body Mass Index (BMI) from weight in kg and height in cm.
    
    Formula: 
        BMI = weight (kg) / (height in meters)^2
    
    Args:
        actual_weight: Weight in kilograms (as string, float, or int).
        height: Height in centimeters (as string, float, or int).
        
    Returns:
        Optional[str]: Formatted string "BMI - Category" (e.g., "22.86 - Normal weight"),
                       or None if the inputs are invalid/non-positive.
    """
    try:
        weight_kg = float(weight_kg)
        height_cm = float(height_cm)

        if weight_kg <= 0 or height_cm <= 0:
            return None

        # Convert height from cm to meters
        height_m = height_cm / 100.0
        bmi = round(weight_kg / (height_m ** 2), 2)

        # Standard WHO BMI classifications
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25.0:
            category = "Normal weight"
        elif 25.0 <= bmi < 30.0:
            category = "Overweight"
        else:
            category = "Obese"

        return f"{bmi:.2f} - {category}"

    except (ValueError, TypeError, ZeroDivisionError):
        return None