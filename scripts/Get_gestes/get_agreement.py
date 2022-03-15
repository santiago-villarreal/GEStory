# Importing the modules
import openpyxl

# Loading the Excel file
pxl_doc = openpyxl.load_workbook('GES267-GesturesV2.xlsx')
sheet = pxl_doc['RefGes']

def get_agreement(d, row):
    # agreement
    cell_obj = sheet.cell(row=row, column=7)

    # Get value of cell object using the value attribute
    agreement = cell_obj.value

    if (agreement == None):
        del d["agreement"]
    else:
        d["agreement"] = float(agreement)