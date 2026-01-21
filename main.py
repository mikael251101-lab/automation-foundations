def evaluate_financial_health(savings, expenses):
    if savings <= 0:
        return 'DANGER'
    elif savings < expenses:
        return 'RISKY'
    elif savings >= 2 * expenses:
        return 'SAFE'
    else:
        return 'STABLE'

def give_advice(status):
    messages = []

    if status == 'DANGER':
        messages.append('Emergency: stop investing, focus on survival')
    elif status == 'RISKY':
        messages.append('Reduce expenses or increase income')
    elif status == 'STABLE':
        messages.append('Keep building skills and savings')
    else:
        messages.append('You can invest more aggressively')
    
    return messages

def simulate_months(months):
    monthly_income = 5_000_000
    expenses = 3_500_000
    cash_savings = 0

    for month in range(1, months + 1):
        print(f'\nMonth {month}')

        # 1. calculate savings
        savings = monthly_income - expenses
        cash_savings += savings

        # 2. evaluate financial health
        status = evaluate_financial_health(cash_savings, expenses)

        # 3. get advice
        messages = give_advice(status)

        # 4. print result
        print(' Savings:', cash_savings)
        print(' Status:', status)

        for msg in messages:
            print(' Advice:', msg)

simulate_months(6)