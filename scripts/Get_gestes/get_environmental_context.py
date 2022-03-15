# Importing the modules
import openpyxl

# Loading the Excel file
pxl_doc = openpyxl.load_workbook('GES267-RepresentationV4.xlsx')
sheet = pxl_doc['GES-Gesture_Representation']

Environmental_Context = {"ph": "Physical Objects",
                         "vi": "Virtual Objects"}

def get_environmental_context(d, row):
    # environmental_Context
    cell_obj = sheet.cell(row=row, column=9)

    # Get value of cell object using the value attribute
    environmental_context = cell_obj.value

    if (environmental_context == None):
        del d["environmental_context"]
    else:
        environmental_context_liste = environmental_context.split(",")
        for i in range(len(environmental_context_liste)):
            environmental_context_liste[i] = environmental_context_liste[i].strip()
        i = 0
        while (i < len(environmental_context_liste)):
            if (environmental_context_liste[i] not in Environmental_Context.keys()):
                del environmental_context_liste[i]
            else:
                environmental_context_liste[i] = Environmental_Context[environmental_context_liste[i]]
            i += 1

        if (len(environmental_context_liste) == 0):
            del d["environmental_context"]
        else:
            d["environmental_context"] = environmental_context_liste