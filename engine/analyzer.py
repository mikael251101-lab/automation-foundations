from engine.ai_insights import generate_ai_insight

def analyze_business(income, expenses, cash, investment):
    savings = income - expenses
    net_worth = cash + investment
    runway = cash / expenses if expenses > 0 else float('inf')

    report = {
        "income": int(income),
        "expenses": int(expenses),
        "savings": int(savings),
        "cash": int(cash),
        "investment": int(investment),
        "net_worth": int(net_worth),
        "runway_months": round(runway, 2)
    }

    report["ai_insight"] = generate_ai_insight(report)
    return report