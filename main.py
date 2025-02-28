import pandas as pd
import glob

filepaths = glob.glob("invoices/*.xlsx")

for file in filepaths:
    read_file = pd.read_excel(file, sheet_name="Sheet 1")
    print(read_file)
