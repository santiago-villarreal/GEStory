# Importing the modules
import openpyxl

# Loading the Excel file
pxl_doc = openpyxl.load_workbook('GES267-Studies.xlsx')
sheet = pxl_doc['Gesture Elicitation Studies']

def get_url(d, row):
    # URL
    cell_obj = sheet.cell(row=row, column=11)

    # Get value of cell object using the value attribute
    url = cell_obj.value

    if (url == None):
        del d["url"]
    else:
        d["url"] = url