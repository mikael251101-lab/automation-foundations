def calculate_monthly_savings(income, expenses):
    return income - expenses


def evaluate_financial_health(cash_savings, expenses):
    """
    Runway-based evaluation
    """
    runway = cash_savings / expenses if expenses > 0 else float('inf')

    if runway < 1:
        return 'DANGER'
    elif runway < 3:
        return 'RISKY'
    elif runway < 6:
        return 'STABLE'
    else:
        return 'SAFE'


def give_advice(status):
    if status == 'DANGER':
        return ['Emergency: stop investing, focus on survival']
    elif status == 'RISKY':
        return ['Reduce expenses or increase income']
    elif status == 'STABLE':
        return ['Keep building skills and savings']
    else:
        return ['You can invest more aggressively']


def handle_life_events(month, income, expenses):
    messages = []

    # income grows every 3 months
    if month % 3 == 0:
        income *= 1.05
        messages.append('Income increased!')

    # expenses grow every 6 months
    if month % 6 == 0:
        expenses *= 1.03
        messages.append('Expenses increased!')

    return income, expenses, messages


def process_investment(savings, cash_savings, investment_balance, ratio, rate):
    if savings > 0:
        invest_amount = savings * ratio
        cash_amount = savings - invest_amount
    else:
        invest_amount = 0
        cash_amount = savings

    cash_savings += cash_amount
    investment_balance *= (1 + rate)
    investment_balance += invest_amount

    return cash_savings, investment_balance


def simulate_until_goal():
    income = 5_000_000
    expenses = 3_500_000
    cash = 0
    investment = 0
    goal = 20_000_000
    month = 0

    investment_ratio = 0.30
    investment_rate = 0.05

    while cash + investment < goal:
        month += 1

        # life events
        income, expenses, _ = handle_life_events(month, income, expenses)

        # savings
        savings = calculate_monthly_savings(income, expenses)

        # investment & growth
        cash, investment = process_investment(
            savings, cash, investment, investment_ratio, investment_rate
        )

        # optional debug
        net = cash + investment
        print(f"Month {month} | Net worth: {int(net):,}")

    print("\n🎉 Goal reached!")
    print("Months needed:", month)
    print(f"Final net worth: {int(cash + investment):,}")

simulate_until_goal()