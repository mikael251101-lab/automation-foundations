def get_user_input():
    try:
        income = float(input("Enter monthly income: "))
        expenses = float(input("Enter monthly expenses: "))
        cash = float(input("Enter cash balance: "))
        investment = float(input("Enter investment balance: "))
        return income, expenses, cash, investment
    except ValueError:
        print("❌ Please enter numbers only")
        return get_user_input()


def analyze_business(income, expenses, cash, investment):
    savings = income - expenses
    net_worth = cash + investment
    return savings, net_worth


def evaluate_status(savings, expenses):
    runway = savings / expenses if expenses > 0 else float('inf')

    if runway < 1:
        return 'DANGER', runway
    elif runway < 3:
        return 'RISKY', runway
    elif runway < 6:
        return 'STABLE', runway
    else:
        return 'SAFE', runway


def generate_advice(status):
    if status == 'DANGER':
        return ['Urgent: cut costs and secure cash immediately']
    elif status == 'RISKY':
        return ['Reduce expenses or increase income']
    elif status == 'STABLE':
        return ['Keep savings growth']
    else:
        return ['You can invest more or hire safely']


def generate_report(income, expenses, savings, net_worth, runway, status, advice):
    print("\n===== MONTHLY BUSINESS REPORT =====")
    print("Income:", f"{income:,.0f}")
    print("Expenses:", f"{expenses:,.0f}")
    print("Savings:", f"{savings:,.0f}")
    print("Net worth:", f"{net_worth:,.0f}")
    print(f"Runway: {runway:.2f} months")
    print("Status:", status)

    for msg in advice:
        print("Advice:", msg)


def main():
    income, expenses, cash, investment = get_user_input()
    savings, net_worth = analyze_business(income, expenses, cash, investment)
    status, runway = evaluate_status(savings, expenses)
    advice = generate_advice(status)

    generate_report(
        income, expenses, savings, net_worth, runway, status, advice
    )


main()