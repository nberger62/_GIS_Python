# Add comments - including script name, your name, date created, script description, etc.
# Name: Nathan Berger
# Script Name: Mod4A_NAB.py
# Class: GIS Programming
# Date: 6/07/2021
        # Script Description: This script creates a new file geodatabase,
        # then copies all of the data (shapefiles) from one folder into the geodatabase,
        # then we iterate through the cities point layer for cities that are county Seats with a for loop,
        # and we search for those cities.
        # We then print them out with the city name, county seat field attribute,
        # and the population of that city.

# Import modules and classes, and set overwriteOutput
print("Importing modules! Let's get this party started :)")
import arcpy
import os
print(arcpy.GetMessages() + "\n")

print("Setting up my work environment!")
print(arcpy.GetMessages() + "\n")
from arcpy import env

env.overwriteOutput = True
env.workspace = r"C:\Users\Admin\PycharmProjects\UWF\Module_4\Data\Mod4_Data"

# Create geodatabase in Module4/Results folder
print("Creating a new file Geo Database called mod4FGDB... (This will be used to copy our data...)")
print(arcpy.GetMessages() + "\n")

print("New Geodatabase created!")
arcpy.CreateFileGDB_management("C:/Users/Admin/PycharmProjects/UWF/Module_4/Results", "mod4FGDB.gdb")
print(arcpy.GetMessages() + "\n")
print("************************************************************************************")


# Define fclist variable to list all feature classes in current workspace
#print
print("Now we will list all of our feature classes in our current workspace (Iterate over our list)...")
print(arcpy.GetMessages() + "\n")
fclist = arcpy.ListFeatureClasses()
print(arcpy.GetMessages() + "\n")

# Create for loop to copy all features from Data folder to new fGDB
print("Now we are actually going to copy the data using a for loop!")
print("************************************************************************************")
print("Copying Features now...")
print("\n")
for fcs in fclist:
    desc = arcpy.da.Describe(fcs)
    outfc = os.path.join("C:/Users/Admin/PycharmProjects/UWF/Module_4/Results/mod4FGDB.gdb", desc["baseName"])
    arcpy.CopyFeatures_management(fcs, outfc)
    print("Copying "+ desc["name"] + "...")
    print(arcpy.GetMessages() + "\n")

# Create a Search Cursor for the cities layer to find the Name, Population (POP_2000), and Feature of
# all cities listed as 'County Seat' in the Feature field.
fc = "C:/Users/Admin/PycharmProjects/UWF/Module_4/Results/mod4FGDB.gdb/cities"
fields = ['NAME', 'FEATURE', 'POP_2000']
where = arcpy.AddFieldDelimiters(fc, 'FEATURE') + " = 'County Seat'"

with arcpy.da.SearchCursor(fc, fields, where) as cursor:
    # Create an empty dictionary
    print("All features copied to the new file geodatabse!")
    county_seats = {}

    # Populate dictionary with names (key) and populations (value) of each 'County Seat' city
    print("\n")
    print("**************************************************************************************")
    print("Iterating Over Cursor Now...")
    print("\n")
    # Print the cities we are iterating over with other metadata

    for row in cursor:
        county_seats[row[0]] = row[2]
        print("City Name: " + str(row[0]))
        print("Feature Type: " + str(row[1]))
        print("Population circa 2000: " + str(row[2]))
        print("\n")

    # Print populated dictionary
    print("\n")
    print("**************************************************************************************")
    print("\n")
    print("Designing and populating the county_seats dictionary! This dictionary will return cities and their population for county seats cities")
    print("\n")
    print("Dictionary complete! See the completed results below...")
    print(arcpy.GetMessages() + "\n")
    print(county_seats)
    print(county_seats["Las Vegas"])

del cursor



