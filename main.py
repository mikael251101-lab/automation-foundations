from interface.input_handler import load_businesses_from_csv
from engine.analyzer import analyze_business
from reports.printer import print_report
from reports.pdf_generator import generate_pdf


def main():
    businesses = load_businesses_from_csv("data/business_data.csv")

    for i, business in enumerate(businesses, start=1):
        result = analyze_business(business)

        print_report(business, result)
        generate_pdf(business, result, i)


if __name__ == "__main__":
    main()
