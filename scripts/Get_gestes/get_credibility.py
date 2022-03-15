# Importing the modules
import openpyxl

# Loading the Excel file
pxl_doc = openpyxl.load_workbook('GES267-GesturesV2.xlsx')
sheet = pxl_doc['RefGes']

def get_credibility(d, row):
    # credibility
    cell_obj = sheet.cell(row=row, column=14)

    # Get value of cell object using the value attribute
    credibility = cell_obj.value

    if (credibility == None):
        del d["credibility"]
    else:
        d["credibility"] = float(credibility)