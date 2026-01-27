from engine import analyze_business

def get_user_input():
    try:
        return (
            float(input("Income: ")),
            float(input("Expenses: ")),
            float(input("Cash: ")),
            float(input("Investment: "))
        )
    except ValueError:
        print("❌ Numbers only")
        return get_user_input()


def print_report(result):
    print("\n===== BUSINESS REPORT =====")
    print(f"Income: {int(result['income']):,}")
    print(f"Expenses: {int(result['expenses']):,}")
    print(f"Savings: {int(result['savings']):,}")
    print(f"Cash: {int(result['cash']):,}")
    print(f"Investment: {int(result['investment']):,}")
    print(f"Net Worth: {int(result['net_worth']):,}")
    print(f"Runway: {result['runway']} months")
    print(f"Status: {result['status']}")