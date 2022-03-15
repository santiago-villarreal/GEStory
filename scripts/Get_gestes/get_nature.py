# Importing the modules
import openpyxl

# Loading the Excel file
pxl_doc = openpyxl.load_workbook('GES267-GesturesV2.xlsx')
sheet = pxl_doc['RefGes']

Nature = {"d": "Deictic",
          "i": "Iconic",
          "m": "Miming",
          "p": "Physical"}

def get_nature(d, row):
    # Nature
    cell_obj = sheet.cell(row=row, column=11)

    # Get value of cell object using the value attribute
    nature = cell_obj.value

    if (nature == None):
        del d["nature"]
    else:
        if (nature not in Nature.keys()):
            del d["nature"]
        else:
            d["nature"] = Nature[nature]