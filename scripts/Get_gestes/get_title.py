# Importing the modules
import openpyxl

# Loading the Excel file
pxl_doc = openpyxl.load_workbook('GES267-Studies.xlsx')
sheet = pxl_doc['Gesture Elicitation Studies']

def get_title(d, row):
    # Title
    cell_obj = sheet.cell(row=row, column=6)

    # Get value of cell object using the value attribute
    title = cell_obj.value

    if (title == None):
        del d["title"]
    else:
        d["title"] = title