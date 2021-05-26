###################################
# Script: Mod2_Script3_NAB_Final.py
# Name: Nathan Berger
# Contact email: nab45@students.uwf.edu
# Date: 5/25/2021
###################################

import arcpy

# Part A: Turn on labels and visibility for layer in TravisCountyAustinTx.aprx
print ("Running Part A...")
aprx = "S:/GISProgramming/Module3/Data/TravisCountyAustinTx.aprx"
try:
    project = arcpy.mp.ArcGISProject()
    lyrlist = project.listMaps()
    for lyr in lyrlist:
	    if lyr.name == "parks":
		    print (lyr.name)
		    lyr.visible = True
		    lyr.showLabels = True
    project.save()
    del project
    del lyrlist
except Exception as e:
    print(e)

print ("Part A successfully completed.")

    
# Part B: Print layer info for TravisCountyAustinTx.aprx
print ("\nRunning Part B...")

proj = r"C:\Users\Admin\PycharmProjects\UWF\Module_2\Data\Mod2_Data\TravisCountyAustinTX.aprx"
project = arcpy.mp.ArcGISProject(proj)
maplist = project.listMaps("Layers")[0]
for df in maplist.listLayers():
    spatial_ref = arcpy.Describe(df).spatialReference
    sr = spatial_ref.PCSName
    code = spatial_ref.PCSCode
    print ("Name:", df.name)
    print ("Data source:", df.dataSource)
    print ("Spatial Reference:", sr + " [Code:", str(code) + "]\n")
del project
print ("Part B successfuly completed.")
