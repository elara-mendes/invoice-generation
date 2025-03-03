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
    invoice_nr, date_invoice = filename.split("-")

    pdf.set_font(style="B", family="Times", size=16)
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}")
    pdf.ln(10)
    pdf.cell(w=50, h=8, txt=f"Date: {date_invoice}", ln=1)

    pdf.ln(15)

    # Header
    columns_items = list(read_file.columns)
    columns = [str(column).replace("_", " ").title() for column in columns_items]

    pdf.set_font(family="Times", size=9, style="B")
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=45, h=8, txt=columns[1], border=1)
    pdf.cell(w=30, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1, ln=1)

    # print(str(columns).replace("_", " ").title())

    # Rows
    for index, row in read_file.iterrows():
        pdf.set_font(family="Times", size=9)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=45, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    total_price = read_file["total_price"].sum()
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=45, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_price), border=1, ln=1)
    # print(total_price)

    # Total Price
    pdf.ln(15)
    pdf.set_font(style="B", family="Times", size=16)
    pdf.cell(w=50, h=8, txt=f"The total price is {total_price}", ln=1)

    pdf.ln(10)
    pdf.cell(w=50, h=8, txt=f"Elarinha Relatórios")
    pdf.image("pythonhow.png", w=10)

    pdf.output(f"pdfs/{filename}.pdf")
    # print(date_invoice)

