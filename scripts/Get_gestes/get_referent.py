# Importing the modules
import openpyxl

# Loading the Excel file
pxl_doc = openpyxl.load_workbook('GES267-GesturesV2.xlsx')
sheet = pxl_doc['RefGes']

def get_referent(d, row):
    # Referent
    cell_obj = sheet.cell(row=row, column=3)

    # Get value of cell object using the value attribute
    referent = cell_obj.value

    if (referent == None):
        del d["referent"]
    else:
        if (type(referent) is int):
            d["referent"] = referent
        else:
            if (referent[len(referent) - 1] == ","):
                referent = referent[:len(referent) - 1]
            referent = referent.strip()
            d["referent"] = referent