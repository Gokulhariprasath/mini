def rule_analysis(data):
    advice = []

    # ---------------- BMI Formula to calculate the body weight----------------
    height_m = data.height / 100    

    bmi = data.weight / (height_m * height_m)

    if bmi < 18.5:
        advice.append("Underweight: Increase nutritious calorie intake")
    elif bmi < 25:
        advice.append("Normal weight: Maintain healthy lifestyle")
    elif bmi < 30:
        advice.append("Overweight: Increase physical activity and control diet")
    elif bmi < 40:
        advice.append("Obese: Strong lifestyle changes required")
    else:
        advice.append("Morbid obesity: Consult a doctor immediately")

    # ---------------- Sleep ----------------
    sleep = data.sleep_hours

    if sleep < 5:
        advice.append("Severe sleep deprivation: High risk to health")
    elif sleep < 6:
        advice.append("Poor sleep: Increase sleep duration urgently")
    elif sleep < 7:
        advice.append("Slightly low sleep: Improve sleep consistency")
    elif sleep <= 9:
        advice.append("Good sleep duration")
    else:
        advice.append("Oversleeping: Maintain balanced sleep schedule")

    # ---------------- Calories ----------------
    calories = data.calories

    if calories < 1200:
        advice.append("Very low calorie intake: May cause nutrient deficiency")
    elif calories < 1800:
        advice.append("Low calorie intake: Ensure adequate nutrition")
    elif calories <= 2500:
        advice.append("Healthy calorie intake")
    elif calories <= 3000:
        advice.append("High calorie intake: Reduce processed foods")
    else:
        advice.append("Very high calorie intake: Strongly reduce calories")

    return advice
