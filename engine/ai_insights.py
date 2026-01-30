from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_ai_insight(data):
    prompt = f"""
You are a business financial analyst.

Analyze this business data and return:
1. 3 bullet insights
2. 1 clear recommendation
3. 1 risk warning (if any)

Business data:
Income: {data['income']}
Expenses: {data['expenses']}
Savings: {data['savings']}
Cash: {data['cash']}
Investment: {data['investment']}
Net Worth: {data['net_worth']}
Runway Months: {data['runway_months']}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text