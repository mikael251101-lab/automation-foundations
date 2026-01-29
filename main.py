from interface.input_handler import get_business_inputs, load_businesses_from_csv
from engine.analyzer import analyze_business
from reports.printer import generate_pdf_report


def main():
    choice = input("Choose input method (manual / csv): ").lower()

    if choice == "manual":
        income, expenses, cash, investment = get_business_inputs()
        result = analyze_business(income, expenses, cash, investment)
        path = generate_pdf_report(result)
        print("📄 PDF saved to:", path)

    elif choice == "csv":
        businesses = load_businesses_from_csv("data/business_data.csv")

        for i, b in enumerate(businesses, 1):
            result = analyze_business(
                b["income"], b["expenses"], b["cash"], b["investment"]
            )
            path = generate_pdf_report(result, i)
            print(f"📄 PDF {i} saved to:", path)

    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()