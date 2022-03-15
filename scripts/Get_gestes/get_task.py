# Importing the modules
import openpyxl

# Loading the Excel file
pxl_doc = openpyxl.load_workbook('GES267-GesturesV2.xlsx')
sheet = pxl_doc['RefGes']

def get_task(d, row):
    # Task
    cell_obj = sheet.cell(row=row, column=4)

    # Get value of cell object using the value attribute
    task = cell_obj.value

    if (task == None):
        del d["task"]
    else:
        liste_task = task.split(",")
        for i in range(len(liste_task)):
            liste_task[i] = liste_task[i].strip().capitalize()
        d["task"] = liste_task