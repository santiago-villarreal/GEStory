# Importing the modules
import openpyxl

# Loading the Excel file
pxl_doc = openpyxl.load_workbook('GES267-Studies.xlsx')
sheet = pxl_doc['Gesture Elicitation Studies']

cas = ["body", "head", "torso", "arm", "wrist", "hand", "finger", "waist", "legs", "foot"]

def get_body(d, row):
    # Body
    cell_obj = sheet.cell(row=row, column=40)

    # Get value of cell object using the value attribute
    body = cell_obj.value

    if (body == None):
        del d["body"]
    else:
        body = body.replace(",", "")
        body_liste = body.split()
        for i in range(len(body_liste)):
            body_liste[i] = body_liste[i].lower().replace(".", "")
        if "arm" in body_liste:
            d["body"] = "arm"
            return
        elif "hand" in body_liste:
            d["body"] = "hand"
            return
        elif "finger" in body_liste:
            d["body"] = "finger"
            return
        else:
            d["body"] = body_liste[0]