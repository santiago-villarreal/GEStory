# Importing the modules
import openpyxl

# Loading the Excel file
pxl_doc = openpyxl.load_workbook('GES267-GesturesV2.xlsx')
sheet = pxl_doc['RefGes']

Locale = {"o": "On-the-object",
          "i": "In-the-air",
          "m": "Mixed"}

def get_locale(d, row):
    # Locale
    cell_obj = sheet.cell(row=row, column=13)

    # Get value of cell object using the value attribute
    locale = cell_obj.value

    if (locale == None):
        del d["locale"]
    else:
        if (locale not in Locale.keys()):
            del d["locale"]
        else:
            d["locale"] = Locale[locale]