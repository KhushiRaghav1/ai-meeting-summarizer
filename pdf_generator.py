from fpdf import FPDF

def generate_pdf(title, summary, actions):

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Meeting Summary Report", ln=True)

    pdf.ln(10)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, f"Meeting Title: {title}", ln=True)

    pdf.ln(5)

    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 8, f"Summary:\n{summary}")

    pdf.ln(5)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Action Items:", ln=True)

    pdf.set_font("Arial", "", 12)

    for action in actions:
        pdf.cell(0, 8, f"- {action}", ln=True)

    filename = "meeting_summary.pdf"
    pdf.output(filename)

    return filename