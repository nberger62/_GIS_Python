# Add comments - including script name, your name, date created, script description, etc.
# Name: Nathan Berger
# Script Name: Mod4A_NAB.py
# Class: GIS Programming
# Date: 6/07/2021
# Script Description:

# Import modules and classes, and set overwriteOutput
print("Importing modules! Let's get this party started :)")
import arcpy
import os

print("setting up my work environment!")
from arcpy import env

env.overwriteOutput = True
env.workspace = r"C:\Users\Admin\PycharmProjects\UWF\Module_4\Data\Mod4_Data"

# Create geodatabase in Module4/Results folder
arcpy.CreateFileGDB_management("C:/Users/Admin/PycharmProjects/UWF/Module_4/Results", "mod4FGDB.gdb")
print(arcpy.GetMessages())

# Define fclist variable to list all feature classes in current workspace
#print
fclist = arcpy.ListFeatureClasses()
print(arcpy.GetMessages())

# Create for loop to copy all features from Data folder to new fGDB
for fcs in fclist:
    desc = arcpy.da.Describe(fcs)
    outfc = os.path.join("C:/Users/Admin/PycharmProjects/UWF/Module_4/Results/mod4FGDB.gdb", desc["baseName"])
    arcpy.CopyFeatures_management(fcs, outfc)
print(arcpy.GetMessages())

# Create a Search Cursor for the cities layer to find the Name, Population (POP_2000), and Feature of
# all cities listed as 'County Seat' in the Feature field.
fc = "C:/Users/Admin/PycharmProjects/UWF/Module_4/Results/mod4FGDB.gdb/cities"
fields = ['NAME', 'FEATURE', 'POP_2000']
where = arcpy.AddFieldDelimiters(fc, 'FEATURE') + " = 'County Seat'"

with arcpy.da.SearchCursor(fc, fields, where) as cursor:
    # Create an empty dictionary
    county_seats = {}

    # Populate dictionary with names (key) and populations (value) of each 'County Seat' city
    for row in cursor:
        county_seats[row[0]] = row[2]

    # Print populated dictionary
    print(county_seats)

del cursor