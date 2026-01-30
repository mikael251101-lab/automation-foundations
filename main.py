from interface.input_handler import load_businesses_from_csv
from engine.analyzer import analyze_business
from reports.printer import generate_pdf_report
from reports.mailer import send_email

def main():
    businesses = load_businesses_from_csv("data/business_data.csv")

    for i, business in enumerate(businesses, start=1):
        try:
            result = analyze_business(
                business["income"],
                business["expenses"],
                business["cash"],
                business["investment"]
            )

            pdf_path = generate_pdf_report(result, i)

            send_email(
                to_email=business["email"],
                subject=f"Financial Report - {business['name']}",
                body="Your report is attached.",
                attachment=pdf_path
            )

            print(f"✅ Report sent for {business['name']}")

        except Exception as e:
            print(f"❌ Failed for {business['name']}:", e)

if __name__ == "__main__":
    main()