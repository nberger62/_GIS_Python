###################################
# Script: Mod2_Script1_NAB.py
# Name: Nathan Berger
# Contact email: nab45@students.uwf.edu
# Date: 5/24/2021
###################################

import arcpy
from arcpy import env
env.workspace = r"C:\Users\Admin\PycharmProjects\UWF\Module_2\Data\Mod2_Data"
fc = "parks.shp"
rows = arcpy.SearchCursor(fc)
fields = arcpy.ListFields(fc)
for field in fields:
    print("Name = {0}".format(field.name))

# Results is below


# Name = FID
# Name = Shape
# Name = PARK_ID
# Name = PARK_NAME
# Name = PARK_TYPE
# Name = SHAPE_AREA
# Name = SHAPE_LEN


