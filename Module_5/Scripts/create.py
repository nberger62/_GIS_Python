import arcpy, fileinput, string, os
from arcpy import env
env.workspace = "S:/GISProgramming/Module6"
env.overwriteOutput = True
outpath = "S:/GISProgramming/Module6/Results"
newfc = "newpolyline.shp"
infile = "S:/GISProgramming/Module6/Data/coordinates.txt"
arcpy.CreateFeatureclass_management(outpath, newfc, "Polyline")
cursor = arcpy.da.InsertCursor(newfc, ["SHAPE@"])
array = arcpy.Array()
a = open(infile,"r")
doc = a.readlines()
for line in doc:
    ID, X, Y = str.split(line, " ")
    array.add(arcpy.Point(X,Y))
    cursor.insertRow([arcpy.Polyline(array)])
fileinput.close()
del cursor
