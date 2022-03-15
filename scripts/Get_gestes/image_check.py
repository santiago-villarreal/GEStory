# Importing the modules
import openpyxl
from openpyxl_image_loader import SheetImageLoader


# Loading the Excel File and the sheet for images
pxl_doc_images = openpyxl.load_workbook('GES267-GesturesV2.xlsx')
sheet_images = pxl_doc_images['RefGes']

# Calling the image_loader
image_loader = SheetImageLoader(sheet_images)

liste_images = []

with open("Images_location.txt", "r") as file:
    for line in file:
        liste_images.append(line.strip())


def image_check(d, cell, count):
    not_image = False
    try:
        image = image_loader.get(cell)
    except ValueError:
        not_image = True
    if (not_image):
        del d["image"]
        return False
    else:
        d["image"] = liste_images[count]
        return True