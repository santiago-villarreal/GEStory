# Importing the modules
import openpyxl

# Loading the Excel file
pxl_doc = openpyxl.load_workbook('GES267-Studies.xlsx')
sheet = pxl_doc['Gesture Elicitation Studies']

def get_published(d, row):
    # Published
    cell_obj = sheet.cell(row=row, column=27)

    # Get value of cell object using the value attribute
    published = cell_obj.value

    if (published == None):
        del d["published"]
    else:
        d["published"] = published