# Importing the modules
import openpyxl

# Loading the Excel file
pxl_doc = openpyxl.load_workbook('GES267-GesturesV2.xlsx')
sheet = pxl_doc['RefGes']

def get_name(d, row):
    # Name
    cell_obj = sheet.cell(row=row, column=5)

    # Get value of cell object using the value attribute
    name = cell_obj.value

    if (name == None):
        del d["name"]
        return False
    else:
        d["name"] = name.capitalize()
        return True