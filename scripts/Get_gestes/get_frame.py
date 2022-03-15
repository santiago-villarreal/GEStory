# Importing the modules
import openpyxl

# Loading the Excel file
pxl_doc = openpyxl.load_workbook('GES267-RepresentationV4.xlsx')
sheet = pxl_doc['GES-Gesture_Representation']

Frame = {"s": "Single",
         "m": "Multi"}

def get_frame(d, row):
    # Frame
    cell_obj = sheet.cell(row=row, column=7)

    # Get value of cell object using the value attribute
    frame = cell_obj.value

    if (frame == None):
        del d["frame"]
    else:
        frame_liste = frame.split(",")
        for i in range(len(frame_liste)):
            frame_liste[i] = frame_liste[i].strip()
        i = 0
        while (i < len(frame_liste)):
            if (frame_liste[i] not in Frame.keys()):
                del frame_liste[i]
            else:
                frame_liste[i] = Frame[frame_liste[i]]
            i += 1

        if (len(frame_liste) == 0):
            del d["frame"]
        else:
            d["frame"] = frame_liste