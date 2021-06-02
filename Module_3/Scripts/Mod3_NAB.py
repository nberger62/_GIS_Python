# Name: Nathan Berger
# Date: 6/1/2021
# Class:
# Script Name:
#----------------------------------------------------------
# import modules
import arcpy

# Set up Workspace Environment

arcpy.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\Admin\PycharmProjects\UWF\Module_3\Data\Mod3_Data"

# Step 1: I need to run the tool for Adding X,Y coordinates to my shapefile called hospitals
# This step needs to have the input shapefile, and set the output shapefile by copyign the data and then adding the points.
arcpy.Copy_management("hospitals.shp", "hospitalsXYpts.shp")
print("Adding XY Coordinates to the shapefile...")
for i in range(0, arcpy.GetMessageCount()):
    arcpy.AddReturnMessage(i)

arcpy.AddXY_management("hospitalsXYpts.shp")
print("hospitalsXYpts.shp \n")

print("Executing buffer analysis on the shapefile...")
for i in range(0, arcpy.GetMessageCount()):
    arcpy.AddReturnMessage(i)

# Now we are going to run an arcpy analysis tool to buffer 1,000 meters around the hosptials we identified earlier in the script

arcpy.analysis.Buffer("hospitalsXYpts.shp", "hosXY_buffer", 1000)
print("hosXY_buffer \n")

print("Executing the dissolve analysis on the shapefile...")
for i in range(0, arcpy.GetMessageCount()):
    arcpy.AddReturnMessage(i)

# Now we can dissolve the buffer around the hospitals into it's own feature class file saved into our project's GDB

with arcpy.EnvManager(scratchWorkspace=r"C:\Users\Admin\PycharmProjects\UWF\Module_3\Data\Mod3_Data\Mod3_NAB\Mod3_NAB.gdb", workspace=r"C:\Users\Admin\PycharmProjects\UWF\Module_3\Data\Mod3_Data\Mod3_NAB\Mod3_NAB.gdb"):
    arcpy.management.Dissolve(r"C:\Users\Admin\PycharmProjects\UWF\Module_3\Data\Mod3_Data\hosXY_buffer.shp", r"C:\Users\Admin\PycharmProjects\UWF\Module_3\Data\Mod3_Data\Mod3_NAB\Mod3_NAB.gdb\hosXY_buffer_Dissolve", None, None, "MULTI_PART", "DISSOLVE_LINES")
print("hosXY_buffer_dissolve \n")

for i in range(0, arcpy.GetMessageCount()):
    arcpy.AddReturnMessage(i)