def analyze_business(business):
    income = business["income"]
    expenses = business["expenses"]
    cash = business["cash"]
    investment = business["investment"]

    savings = income - expenses
    net_worth = cash + investment

    return {
        "savings": savings,
        "net_worth": net_worth
    }