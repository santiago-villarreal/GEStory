# Importing the modules
import openpyxl

# Loading the Excel file
pxl_doc = openpyxl.load_workbook('GES267-RepresentationV4.xlsx')
sheet = pxl_doc['GES-Gesture_Representation']

Perspective = {"1p": "1st Person",
               "3p": "3rd Person",
               "mi": "Mirror",
               "bi": "Bird's eye",
               "si": "Side angle"}

def get_perspective(d, row):
    # Perspective
    cell_obj = sheet.cell(row=row, column=6)

    # Get value of cell object using the value attribute
    perspective = cell_obj.value

    if (perspective == None):
        del d["perspective"]
    else:
        perspective_liste = perspective.split(",")
        for i in range(len(perspective_liste)):
            perspective_liste[i] = perspective_liste[i].strip()

        i = 0
        while (i < len(perspective_liste)):
            if (perspective_liste[i] not in Perspective.keys()):
                del perspective_liste[i]
            else:
                perspective_liste[i] = Perspective[perspective_liste[i]]
            i += 1

        if (len(perspective_liste) == 0):
            del d["perspective"]
        else:
            d["perspective"] = perspective_liste