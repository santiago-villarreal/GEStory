# Importing the modules
import openpyxl

# Loading the Excel file
pxl_doc = openpyxl.load_workbook('GES267-RepresentationV4.xlsx')
sheet = pxl_doc['GES-Gesture_Representation']

Gesture_Elements = {"1s": "1-Sided Arrow",
                    "2s": "2-Sided Arrow",
                    "do": "Dotted lines",
                    "gh": "Ghost",
                    "fi": "Finger Trail",
                    "ot": "Other motion lines",
                    "to": "Touchpoints",
                    "te": "Text",
                    "nu": "Numbers",
                    "be": "Bending joints",
                    "ax": "Axis"}

def get_gesture_elements(d, row):
    # Gesture_Elements
    cell_obj = sheet.cell(row=row, column=11)

    # Get value of cell object using the value attribute
    gesture_elements = cell_obj.value

    if (gesture_elements == None):
        del d["gesture_elements"]
    else:
        gesture_elements_liste = gesture_elements.split(",")
        for i in range(len(gesture_elements_liste)):
            gesture_elements_liste[i] = gesture_elements_liste[i].strip()
        i = 0
        while (i < len(gesture_elements_liste)):
            if (gesture_elements_liste[i] not in Gesture_Elements.keys()):
                del gesture_elements_liste[i]
            else:
                gesture_elements_liste[i] = Gesture_Elements[gesture_elements_liste[i]]
            i += 1
        if (len(gesture_elements_liste) == 0):
            del d["gesture_elements"]
        else:
            d["gesture_elements"] = gesture_elements_liste