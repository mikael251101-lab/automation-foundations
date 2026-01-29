from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from textwrap import wrap
import os

def draw_multiline_text(c, text, x, y, max_width=90, line_height=15):
    lines = wrap(text, max_width)

    for line in lines:
        if y < 50:  # new page
            c.showPage()
            c.setFont("Helvetica", 12)
            y = 800

        c.drawString(x, y, line)
        y -= line_height

    return y

def generate_pdf_report(data, index):
    """
    Generate a single PDF report for one business
    """

    output_dir = "reports/output"
    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(output_dir, f"business_{index}.pdf")

    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    y = height - 60

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Business Financial Report")
    y -= 40

    # Financial data
    c.setFont("Helvetica", 12)
    for key, value in data.items():
        if key == "ai_insight":
            continue  # skip for now

        label = key.replace("_", " ").title()

        if isinstance(value, (int, float)):
            value = f"{value:,}"

        c.drawString(50, y, f"{label}: {value}")
        y -= 22

    # ==========================
    # ✅ ADD AI INSIGHT HERE
    # ==========================
    if "ai_insight" in data:
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, "AI Insights:")
        y -= 20

        c.setFont("Helvetica", 11)
        y = draw_multiline_text(
            c,
            data["ai_insight"],
            x=60,
            y=y
        )

    # Save PDF
    c.save()

    return file_path