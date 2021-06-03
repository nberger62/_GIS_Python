# Name: Nathan Berger
# Date: 6/1/2021
# Class: GIS Programming
# Script Name: Mod3_NAB.py
# Description:
# This Python script takes a shapefile of hospitals, adds XY coordinates or LAT/Long's to the points,
# then establishes a buffer of 1000 meters around the hospitals,
# and the dissolves the buffer to make sure lines do not overlap the buffered area around the hospitals.
# Each step is logged in the terminal with the script's start time, end time, and the tool's name that is running at that point in time.
#----------------------------------------------------------

# import modules
import arcpy

# Set up Workspace Environment
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\Admin\PycharmProjects\UWF\Module_3\Data\Mod3_Data"

# I need to run the tool for Adding X,Y (Longitude and Lattitude) coordinates to my shapefile called hospitals.
# I will copy the shapefile first and then add the coordinates.
# This step needs to have the input shapefile, and set the output shapefile by copying the data and then adding the points.
arcpy.Copy_management("hospitals.shp", "hospitalsXYpts.shp")
print("Adding XY Coordinates to the shapefile...")
arcpy.AddXY_management("hospitalsXYpts.shp")
print(arcpy.GetMessages() + "\n")

# Now we are going to run an arcpy analysis tool to buffer 1,000 meters around the hosptials we identified earlier in the script.
print("Executing buffer analysis on the shapefile...")
arcpy.analysis.Buffer("hospitalsXYpts.shp", "hosXY_buffer", "1000 Meters")
print(arcpy.GetMessages() + "\n")

# Now we can dissolve the buffer around the hospitals into it's own feature class file saved into our project's GDB.
# The dissolve tool will elimanate any overlapping lines that the buffer ranges have created around the hospitals.
print("Executing the dissolve analysis on the shapefile...")
arcpy.management.Dissolve("hosXY_buffer.shp", "hosXY_buffer_Dissolve", None, None, "MULTI_PART", "DISSOLVE_LINES")
print(arcpy.GetMessages() + "\n")