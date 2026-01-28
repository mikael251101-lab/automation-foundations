from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

def generate_pdf(business, result, index):
    os.makedirs("reports/output", exist_ok=True)

    filename = f"reports/output/business_{index}.pdf"
    c = canvas.Canvas(filename, pagesize=A4)

    text = c.beginText(40, 800)
    text.setFont("Helvetica", 11)

    text.textLine("BUSINESS FINANCIAL REPORT")
    text.textLine("-" * 40)
    text.textLine("")
    text.textLine(f"Income: {int(business['income']):,}")
    text.textLine(f"Expenses: {int(business['expenses']):,}")
    text.textLine(f"Savings: {int(result['savings']):,}")
    text.textLine(f"Net Worth: {int(result['net_worth']):,}")

    c.drawText(text)
    c.showPage()
    c.save()

    print(f"📄 PDF generated: {filename}")