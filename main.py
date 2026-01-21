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


def simulate_months(months):
    # base values
    monthly_income = 5_000_000
    expenses = 3_500_000

    cash_savings = 0
    investment_balance = 0

    investment_ratio = 0.30
    investment_rate = 0.05

    history = []

    for month in range(1, months + 1):
        print(f'\nMonth {month}')

        # 1. life events
        monthly_income, expenses, life_messages = handle_life_events(
            month, monthly_income, expenses
        )

        for msg in life_messages:
            print(' ', msg)

        # 2. savings
        savings = calculate_monthly_savings(monthly_income, expenses)
        cash_savings, investment_balance = process_investment(
            savings, cash_savings, investment_balance, investment_ratio, investment_rate
        )

        # 3. health check (RUNWAY BASED)
        status = evaluate_financial_health(cash_savings, expenses)
        advice = give_advice(status)

        # 4. net worth
        net_worth = cash_savings + investment_balance

        # 5. save history
        history.append({
            'month': month,
            'income': int(monthly_income),
            'expenses': int(expenses),
            'savings': int(savings),
            'cash': int(cash_savings),
            'investment': int(investment_balance),
            'net_worth': int(net_worth),
            'status': status,
            'runway_months': round(cash_savings / expenses, 2)
        })

        # 6. print month
        print(' Income:', int(monthly_income))
        print(' Expenses:', int(expenses))
        print(' Savings:', int(savings))
        print(' Cash savings:', int(cash_savings))
        print(' Investment:', int(investment_balance))
        print(' Runway (months):', round(cash_savings / expenses, 2))
        print(' Status:', status)

        for msg in advice:
            print(' Advice:', msg)

        print(' Net worth:', int(net_worth))

    # ===== SUMMARY =====
    print('\n====== SUMMARY FROM HISTORY ======')

    for record in history:
        print(
            f"Month {record['month']} | "
            f"Runway: {record['runway_months']} months | "
            f"Net worth: {record['net_worth']:,} | "
            f"Status: {record['status']}"
        )


simulate_months(6)