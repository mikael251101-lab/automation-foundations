def print_report(business, result):
    print("\n===== BUSINESS REPORT =====")
    print(f"Income: {int(business['income']):,}")
    print(f"Expenses: {int(business['expenses']):,}")
    print(f"Savings: {int(result['savings']):,}")
    print(f"Net Worth: {int(result['net_worth']):,}")