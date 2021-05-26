import arcpy
from arcpy import env
env.workspace = "S:/GISProgramming/Module3/Data"
fclist = arcpy.ListFeatureClasses()
for fc in fclist
    desc = arcpy.describe(fc)
    print(desc.basename + ": " + des.shapeType)
