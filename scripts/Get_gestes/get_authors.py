# Importing the modules
import openpyxl

# Loading the Excel file
pxl_doc = openpyxl.load_workbook('GES267-Studies.xlsx')
sheet = pxl_doc['Gesture Elicitation Studies']

def get_authors(d, row):
    # Authors
    cell_obj = sheet.cell(row=row, column=4)

    # Get value of cell object using the value attribute
    authors = cell_obj.value

    if (authors == None):
        del d["authors"]
    else:
        authors_liste = authors.split(";")
        for i in range(len(authors_liste)):
            authors_liste[i] = authors_liste[i].strip()
        d["authors"] = authors_liste