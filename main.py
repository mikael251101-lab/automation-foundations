def calculate_monthly_savings(income, expenses):
    return income - expenses

def handle_life_events(month, income, base_expenses):
    expenses = base_expenses
    messages = []

    if month == 4:
        income += 500_000
        messages.append('Income increased!')

    if month == 5:
        expenses += 1_000_000
        messages.append('Emergency expense')

    return income, expenses, messages

def process_investment(month, savings, cash_savings, investment_balance, ratio, rate):
    if month == 4:
        invest_amount = savings * ratio
        cash_amount = savings - invest_amount
    else:
        invest_amount = 0
        cash_amount = savings

    cash_savings += cash_amount
    investment_balance += invest_amount
    investment_balance *= (1 + rate)

    return cash_savings, investment_balance

def simulate_months(months):
    monthly_income = 5_000_000
    base_expenses = 3_500_000

    cash_savings = 0
    investment_balance = 0

    investment_ratio = 0.30
    investment_rate = 0.05

    for month in range(1, months + 1):
        monthly_income, expenses, messages = handle_life_events(
            month, monthly_income, base_expenses
        )

        print(f'\nMonth {month}')

        for msg in messages:
            print(' ', msg)

        savings = calculate_monthly_savings(monthly_income, expenses)

        cash_savings, investment_balance = process_investment(
            month,
            savings,
            cash_savings,
            investment_balance,
            investment_ratio,
            investment_rate
        )

        net_worth = cash_savings + investment_balance

        print(' Cash savings:', int(cash_savings))
        print(' Investment balance:', int(investment_balance))
        print(' Net worth:', int(net_worth))

simulate_months(6)