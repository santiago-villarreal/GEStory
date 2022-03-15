# Importing the modules
import openpyxl

# Loading the Excel file
pxl_doc = openpyxl.load_workbook('GES267-GesturesV2.xlsx')
sheet = pxl_doc['RefGes']

Cl_Aigner = {"po": "Pointing",
             "ss": "Semaphoric\nStatic",
             "sd": "Semaphoric\nDynamic",
             "sk": "Semaphoric\nStroke",
             "pa": "Pantomimic",
             "is": "Iconic\nStatic",
             "id": "Iconic\nDynamic",
             "ma": "Manipulation"}

def get_type(d, row):
    # Type
    cell_obj = sheet.cell(row=row, column=8)

    # Get value of cell object using the value attribute
    type = cell_obj.value

    if (type == None):
        del d["type"]
    else:
        if (type not in Cl_Aigner.keys()):
            del d["type"]
        else:
            d["type"] = Cl_Aigner[type]