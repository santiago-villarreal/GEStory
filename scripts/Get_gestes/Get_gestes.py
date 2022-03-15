# Imports
from get_name import get_name
from get_title import get_title
from get_authors import get_authors
from get_published import get_published
from get_year import get_year
from get_url import get_url
from get_user import get_user
from get_location import get_location
from image_check import image_check
from get_body import get_body
from get_task import get_task
from get_referent import get_referent
from get_type import get_type
from get_form import get_form
from get_nature import get_nature
from get_symmetry import get_symmetry
from get_locale import get_locale
from get_perspective import get_perspective
from get_frame import get_frame
from get_body_context import get_body_context
from get_environmental_context import get_environmental_context
from get_color import get_color
from get_gesture_elements import get_gesture_elements
from get_credibility import get_credibility
from get_agreement import get_agreement
import openpyxl
import json


# Loading the Excel File and the sheet for ID check
pxl_doc_id = openpyxl.load_workbook('GES267-GesturesV2.xlsx')
sheet_id = pxl_doc_id['RefGes']

data = []
id_flag = 0
count = 0
# Get all data
for i in range (2, 3912):
#for i in range(2, 3):
    obj_json = {
        "name" : "",
        "title" : "",
        "authors" : [],
        "published" : "",
        "year" : 0,
        "url" : "",
        "user": [],
        "location" : "",
        "image" : "",
        "body" : "",
        "device" : "no-device",
        "environment" : "Unmanned Aerial Vehicle (UAV)",
        "task" : [],
        "referent" : "",
        "type" : "",
        "form" : "",
        "nature" : "",
        "symmetry" : "",
        "locale" : "",
        "perspective" : [],
        "frame" : [],
        "body_context" : [],
        "environmental_context" : [],
        "color" : "",
        "gesture_elements" : [],
        "credibility": 0,
        "agreement": 0}
    cell_obj_id = sheet_id.cell(row=i, column=1).value
    cell = 'F' + str(i)
    if (cell_obj_id != None and cell_obj_id > id_flag):
        id_flag += 1
    if (not get_name(obj_json, i)):
        continue
    get_title(obj_json, id_flag+1)
    get_authors(obj_json, id_flag+1)
    get_published(obj_json, id_flag+1)
    get_year(obj_json, id_flag+1)
    get_url(obj_json, id_flag+1)
    get_user(obj_json, id_flag+1)
    get_location(obj_json, id_flag+1)
    if (image_check(obj_json, cell, count)):
        count += 1
    get_body(obj_json, id_flag+1)
    get_task(obj_json, i)
    get_referent(obj_json, i)
    get_type(obj_json, i)
    get_form(obj_json, i)
    get_nature(obj_json, i)
    get_symmetry(obj_json, i)
    get_locale(obj_json, i)
    get_perspective(obj_json, id_flag+2)
    get_frame(obj_json, id_flag+2)
    get_body_context(obj_json, id_flag+2)
    get_environmental_context(obj_json, id_flag+2)
    get_color(obj_json, id_flag+2)
    get_gesture_elements(obj_json, id_flag+2)
    get_credibility(obj_json, i)
    get_agreement(obj_json, i)
    data.append(obj_json)

with open('data.json', 'w') as json_file:
    json.dump(data, json_file)