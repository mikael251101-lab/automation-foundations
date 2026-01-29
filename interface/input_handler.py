import csv

def get_business_inputs():
    try:
        income = float(input("Enter monthly income: "))
        expenses = float(input("Enter monthly expenses: "))
        cash = float(input("Enter cash balance: "))
        investment = float(input("Enter investment balance: "))
        return income, expenses, cash, investment
    except ValueError:
        print("❌ Please enter numbers only")
        return get_business_inputs()


def load_businesses_from_csv(filename):
    businesses = []
    with open(filename, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            businesses.append({
                "income": float(row["income"]),
                "expenses": float(row["expenses"]),
                "cash": float(row["cash"]),
                "investment": float(row["investment"]),
            })
    return businesses