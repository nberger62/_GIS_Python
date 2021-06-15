####################################
## SCRIPT: Mod5_NAB.py
## NAME: Nathan Alexander Berger
## CONTACT: nab45@students.uwf.edu
## DATE: 6/13/2021
## DESCRIPTION: This script is a python script in ArcPY in which we are taking a shapefile from a data folder pf many shapoefiles and converting them into a text file.
# This text file will contain thew names of rivers, as well as an OID , a vertex ID number, X and Y coordinates, and the name of the rivers.
# The text file will need to be created, as well as a search cursor.
# The script imports modules, sets the workspace env, and then runs through the for loops and processes to make the text file.
# We can check the text file at the end to make sure our code worked properly.
####################################

## Step 1: Setup ##
# import all modules and classes that you need, enable the overwriteOutput setting, set the workspace,
# and define your feature class variable
import arcpy
import os

from arcpy import env

print("Seeting up my script by importing my modules " + "\n")
env.overwriteOutput = True
env.workspace = "C:/Users/Admin/PycharmProjects/UWF/Module_5/Data"
print("Setting up my workspace " + "\n")

## Step 2: Prepare to write .txt file ##
# Create (open) a rivers.txt file for writing ("w"). See Assignment for syntax.
riversTxtName = "C:/Users/Admin/PycharmProjects/UWF/Module_5/Data/rivers_970594643.txt"
riversTxt = open(riversTxtName, 'w')
print("I just created a text file for my rivers in which we will be copying data to the text file!" + "\n")

# Create search cursor for rivers.shp. The cursor should call on the OID, SHAPE, and NAME fields.
infc = r"C:\Users\Admin\PycharmProjects\UWF\Module_5\Data\rivers.shp"

# Enter for loop for each feature
with (arcpy.da.SearchCursor(infc, ["OID@", "NAME", "SHAPE@"])) as cursor:
    for row in cursor:
        vertexId = 0

        for point in row[2].getPart(0):
            vertexId += 1
            print(point)

            riversTxt.write(str(row[0]) + " ")
            riversTxt.write(str(vertexId) + " ")
            riversTxt.write(str(point.X) + " ")
            riversTxt.write(str(point.Y) + " ")
            riversTxt.write(row[1] + " ")
            riversTxt.write("\n")

del cursor
riversTxt.close()