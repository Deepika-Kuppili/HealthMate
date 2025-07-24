from fpdf import FPDF

def sanitize_text(text):
    return str(text).encode("ascii", errors="ignore").decode("ascii")

def generate_pdf(filename, risk, inputs):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="HealthMate - Weekly Health Report", ln=True, align="C")
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Predicted Health Risk: {sanitize_text(risk)}", ln=True)
    pdf.ln(10)
    pdf.cell(200, 10, txt="User Inputs:", ln=True)

    for key, value in inputs.items():
        clean_key = sanitize_text(key)
        clean_value = sanitize_text(value)
        pdf.cell(200, 10, txt=f"{clean_key}: {clean_value}", ln=True)

    pdf.output(filename)
