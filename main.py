from interface.input_handler import load_businesses_from_csv
from engine.analyzer import analyze_business
from reports.printer import print_report


def main():
    businesses = load_businesses_from_csv("data/business_data.csv")

    for i, business in enumerate(businesses, start=1):
        print(f"\n=== BUSINESS #{i} ===")
        result = analyze_business(business)
        print_report(business, result)


if __name__ == "__main__":
    main()