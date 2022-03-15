# Importing the modules
import openpyxl

# Loading the Excel file
pxl_doc = openpyxl.load_workbook('GES267-GesturesV2.xlsx')
sheet = pxl_doc['RefGes']

Symmetry = {"u": "Unilateral",
            "s": "Bilateral-Symmetric",
            "a": "Bilateral-Asymmetric"}

def get_symmetry(d, row):
    # Symmetry
    cell_obj = sheet.cell(row=row, column=12)

    # Get value of cell object using the value attribute
    symmetry = cell_obj.value

    if (symmetry == None):
        del d["symmetry"]
    else:
        if (symmetry not in Symmetry.keys()):
            del d["symmetry"]
        else:
            d["symmetry"] = Symmetry[symmetry]