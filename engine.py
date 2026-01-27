def analyze_business(income, expenses, cash, investment):
    savings = income - expenses
    net_worth = cash + investment
    runway = cash / expenses if expenses > 0 else float("inf")

    if runway < 1:
        status = "DANGER"
    elif runway < 3:
        status = "RISKY"
    elif runway < 6:
        status = "STABLE"
    else:
        status = "SAFE"

    return {
        "income": income,
        "expenses": expenses,
        "savings": savings,
        "cash": cash,
        "investment": investment,
        "net_worth": net_worth,
        "runway": round(runway, 2),
        "status": status
    }