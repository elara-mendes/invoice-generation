import pandas as pd
from fpdf import FPDF
from pathlib import Path
import glob

filepaths = glob.glob("invoices/*.xlsx")

for file in filepaths:
    read_file = pd.read_excel(file, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(file).stem
    invoice_nr = filename.split("-")[0]
    pdf.set_font(style="B", family="Times", size=16)
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}")
    pdf.output(f"pdfs/{filename}.pdf")
