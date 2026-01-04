import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found")

client = genai.Client(api_key=API_KEY)

def get_ai_advice(data):
    """
    Generate NCD-focused lifestyle advice based on user health data.
    
    data: object with attributes
        - calories (float)
        - sleep_hours (float)
        - weight (float, kg)
        - height (float, cm)
    """
    # Convert height to meters for BMI calculation
    height_m = data.height / 100
    bmi = round(data.weight / (height_m ** 2),2)

    # Construct the prompt exactly as your format with NCD conditions
    prompt = f"""
You are a health lifestyle advisor (not a doctor).

Patient data:
- Calories intake per day: {data.calories} kcal
- Sleep duration: {data.sleep_hours} hours
- Weight: {data.weight} kg
- Height: {height_m:.2f} cm
- BMI: {bmi:.1f}

Consider the following NCD conditions:
- Obesity
- Type 2 Diabetes
- Cardiovascular diseases
- Hypertension
- cancer
- Dyslipidemia

Give:
1. Diet advice
2. Sleep improvement advice
3. Physical activity advice
4. Overall health summary
5. prevention for NCD disesses

Rules:
- Do NOT give medical diagnosis
- Use simple language
- Use bullet points
- Keep response under 200 words
"""

    # Generate content from Gemini AI
    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt
    )

    # Return response text
    return response.text  # use response.output_text if your genai version requires

# Example usage
#if __name__ == "__main__":
    #from types import SimpleNamespace
    #test_data = SimpleNamespace(calories=2500, sleep_hours=6, weight=95, height=170)
    #advice = get_ai_advice(test_data)
    #print(advice) 
