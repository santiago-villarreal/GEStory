# Importing the modules
import openpyxl

# Loading the Excel file
pxl_doc = openpyxl.load_workbook('GES267-Studies.xlsx')
sheet = pxl_doc['Gesture Elicitation Studies']

def get_year(d, row):
    # Year
    cell_obj = sheet.cell(row=row, column=3)

    # Get value of cell object using the value attribute
    year = cell_obj.value

    if (year == None):
        del d["year"]
    else:
        d["year"] = year