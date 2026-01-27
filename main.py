import csv

# ---------------------------
# INPUT
# ---------------------------
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


def read_business_data(filename):
    data = []

    with open(filename, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # normalize headers
            row = {k.strip().lower(): v for k, v in row.items()}

            try:
                row["income"] = float(row["income"])
                row["expenses"] = float(row["expenses"])
                row["cash"] = float(row["cash"])
                row["investment"] = float(row["investment"])
            except KeyError as e:
                print("❌ Missing column in CSV:", e)
                print("👉 Found columns:", list(row.keys()))
                return []

            data.append(row)

    return data


# ---------------------------
# LOGIC
# ---------------------------
def analyze_business(income, expenses, cash, investment):
    savings = income - expenses
    net_worth = cash + investment
    return savings, net_worth


def evaluate_status(savings, expenses):
    runway = savings / expenses if expenses > 0 else float("inf")

    if runway < 1:
        return "DANGER"
    elif runway < 3:
        return "RISKY"
    elif runway < 6:
        return "STABLE"
    else:
        return "SAFE"


def generate_advice(status):
    if status == "DANGER":
        return ["Urgent: cut costs and secure cash immediately"]
    elif status == "RISKY":
        return ["Reduce expenses or increase income"]
    elif status == "STABLE":
        return ["Maintain discipline and optimize growth"]
    else:
        return ["You can invest, hire, or expand safely"]


# ---------------------------
# OUTPUT
# ---------------------------
def print_report(income, expenses, cash, investment):
    savings, net = analyze_business(income, expenses, cash, investment)
    status = evaluate_status(savings, expenses)
    advice = generate_advice(status)

    print("\n===== BUSINESS REPORT =====")
    print(f"Income     : {int(income):,}")
    print(f"Expenses   : {int(expenses):,}")
    print(f"Savings    : {int(savings):,}")
    print(f"Cash       : {int(cash):,}")
    print(f"Investment : {int(investment):,}")
    print(f"Net Worth  : {int(net):,}")
    print(f"Status     : {status}")

    print("\nAdvice:")
    for tip in advice:
        print(f"- {tip}")


# ---------------------------
# MAIN
# ---------------------------
def main():
    print("Business Financial Analyzer")
    print("===========================")
    choice = input("Choose input method (manual / csv): ").lower()

    if choice == "manual":
        income, expenses, cash, investment = get_business_inputs()
        print_report(income, expenses, cash, investment)

    elif choice == "csv":
        data = read_business_data("business_data.csv")
        for i, business in enumerate(data, 1):
            print(f"\n--- Business #{i} ---")
            print_report(
                business["income"],
                business["expenses"],
                business["cash"],
                business["investment"],
            )

    else:
        print("❌ Invalid choice")


if __name__ == "__main__":
    main()