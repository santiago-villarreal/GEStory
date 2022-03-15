# Importing the modules
import openpyxl

# Loading the Excel file
pxl_doc = openpyxl.load_workbook('GES267-Studies.xlsx')
sheet = pxl_doc['Gesture Elicitation Studies']

cas = ["body", "head", "torso", "arm", "wrist", "hand", "finger", "waist", "legs", "foot"]

def get_location(d, row):
    # Location
    cell_obj = sheet.cell(row=row, column=40)

    # Get value of cell object using the value attribute
    location = cell_obj.value

    if (location == None):
        del d["location"]
    else:
        location = location.replace(",", "")
        location_liste = location.split()
        if (len(location_liste) == 0):
            del d["location"]
        else:
            i = 0
            while (i < len(location_liste)):
                location_liste[i] = location_liste[i].lower().replace(".", "")
                if (location_liste[i] not in cas):
                    if ("body" in location_liste[i]):
                        location_liste[i] = "body"
                    else:
                        del location_liste[i]
                i += 1
            if (len(location_liste) == 0):
                del d["location"]
            else:
                if "arm" in location_liste:
                    d["location"] = "arm"
                    return
                elif "hand" in location_liste:
                    d["location"] = "hand"
                    return
                elif "finger" in location_liste:
                    d["location"] = "finger"
                    return
                else:
                    d["location"] = location_liste[0]