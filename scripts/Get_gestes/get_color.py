# Importing the modules
import openpyxl

# Loading the Excel file
pxl_doc = openpyxl.load_workbook('GES267-RepresentationV4.xlsx')
sheet = pxl_doc['GES-Gesture_Representation']

Color = {"y": "yes",
         "n": "no"}

def get_color(d, row):
    # Color
    cell_obj = sheet.cell(row=row, column=10)

    # Get value of cell object using the value attribute
    color = cell_obj.value

    if (color == None):
        del d["color"]
    else:
        if (color not in Color.keys()):
            del d["color"]
        else:
            d["color"] = Color[color]