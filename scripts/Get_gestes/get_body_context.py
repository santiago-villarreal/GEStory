# Importing the modules
import openpyxl

# Loading the Excel file
pxl_doc = openpyxl.load_workbook('GES267-RepresentationV4.xlsx')
sheet = pxl_doc['GES-Gesture_Representation']

Body_Context = {"fu": "Full-Body",
                "lo": "Lower-Body",
                "up": "Upper-body",
                "ot": "Other part body"}

def get_body_context(d, row):
    # Body_Context
    cell_obj = sheet.cell(row=row, column=8)

    # Get value of cell object using the value attribute
    body_context = cell_obj.value

    if (body_context == None):
        del d["body_context"]
    else:
        body_context_liste = body_context.split(",")
        for i in range(len(body_context_liste)):
            body_context_liste[i] = body_context_liste[i].strip()
        i = 0
        while (i < len(body_context_liste)):
            if (body_context_liste[i] not in Body_Context.keys()):
                del body_context_liste[i]
            else:
                body_context_liste[i] = Body_Context[body_context_liste[i]]
            i += 1

        if (len(body_context_liste) == 0):
            del d["body_context"]
        else:
            d["body_context"] = body_context_liste