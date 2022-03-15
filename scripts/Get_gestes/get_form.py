# Importing the modules
import openpyxl

# Loading the Excel file
pxl_doc = openpyxl.load_workbook('GES267-GesturesV2.xlsx')
sheet = pxl_doc['RefGes']

Form = {"s": "Static Gesture",
        "d": "Dynamic Gesture"}

def get_form(d, row):
    # Form
    cell_obj = sheet.cell(row=row, column=9)

    # Get value of cell object using the value attribute
    form = cell_obj.value

    if (form == None):
        del d["form"]
    else:
        if (form not in Form.keys()):
            del d["form"]
        else:
            d["form"] = Form[form]