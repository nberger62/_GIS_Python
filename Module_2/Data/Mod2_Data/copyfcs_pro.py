import arcpy
import os
from arcpy import env
env.workspace = "S:/GISProgramming/Module3/Data/"
fclist = arcpy.ListFeatureclasses()
for fc in fclist:
    desc = arcpy.Describe(fc)
    arcpy.CopyFeatures_management(fc, os.path.join("Results/Study.gdb", desc.basename))
print ("Features have been copied to the file geodatabase.")

  