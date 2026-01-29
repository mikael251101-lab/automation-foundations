from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_ai_insight(report_data):
    prompt = f"""
You are a business analyst.

Given this data:
{report_data}

Provide:
1. 2–3 short insights
2. One clear recommendation
3. One risk warning if any

Keep it concise and professional.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )

    return response.choices[0].message.content