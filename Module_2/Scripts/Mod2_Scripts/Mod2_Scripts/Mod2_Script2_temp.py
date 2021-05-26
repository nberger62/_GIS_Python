###################################
# Script: Mod2
# Name: Nathan Berger
# Contact email: nab45
# Date: 5/25/2021
###################################


# import modules
import arcpy

# define variables
filepath = r"C:\Users\Admin\PycharmProjects\UWF\Module_2\Data\Mod2_Data\TravisCountyAustinTX.aprx"
aprx = arcpy.mp.ArcGISProject(filepath)
maps = aprx.listMaps()

dataset = r"C:\Users\Admin\PycharmProjects\UWF\Module_2\Data\Mod2_Data\parks.shp"
desc = arcpy.Describe(dataset)
spatialRef = desc.spatialReference

# perform analysis
print("The spatial reference for this project is " + spatialRef.name + ".\n")

# For Loops
for m in maps:
    print("This Project's Map contains the following layers: ")
    for lyr in m.listLayers():
        print("This layer's name is called " + str(lyr.name))


# save Project
aprx.save()
del aprx