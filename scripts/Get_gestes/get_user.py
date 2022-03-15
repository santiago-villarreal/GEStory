# Importing the modules
import openpyxl

# Loading the Excel file
pxl_doc = openpyxl.load_workbook('GES267-Studies.xlsx')
sheet = pxl_doc['Gesture Elicitation Studies']

def get_user(d, row):
    # User
    cell_obj = sheet.cell(row=row, column=38)

    # Get value of cell object using the value attribute
    user = cell_obj.value

    if (user == None):
        del d["user"]
    else:
        user = user.replace(",", " ")
        user_liste = user.split()
        d["user"] = user_liste