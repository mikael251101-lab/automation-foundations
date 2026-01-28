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
    
import csv

def load_businesses_from_csv(filename):
    businesses = []

    with open(filename, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row = {k.strip().lower(): float(v) for k, v in row.items()}
            businesses.append(row)

    return businesses