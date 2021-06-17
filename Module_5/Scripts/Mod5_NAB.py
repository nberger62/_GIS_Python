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
print("Creating my rivers text file...")
riversTxtName = "C:/Users/Admin/PycharmProjects/UWF/Module_5/Data/rivers_970594643.txt"
riversTxt = open(riversTxtName, 'w')
print("I just created a text file for my rivers in which we will be copying data to the text file!" + "\n")
infc = r"C:\Users\Admin\PycharmProjects\UWF\Module_5\Data\rivers.shp"

# Create search cursor for rivers.shp. The cursor should call on the OID, SHAPE, and NAME fields.
print("Creating My search Cursor for my rivers shapefile!")
with (arcpy.da.SearchCursor(infc, ["OID@", "NAME", "SHAPE@"])) as cursor:

    ## Step 3: Write to .txt file using for loops ##
    # Step 3a: First, iterate through each row/feature in the cursor/ShapeFile
    # Create a variable here to act as a vertex ID number.
    # for every row in the cursor
    for row in cursor:
        # create the vertex id at 0
        vertexId = 0
        # Step 3b: Iterate through each point or vertex in the row. Remember to add the .getPart() method.
        # Create for loop"
        # for part in row[2]:
        #     for point in part:
        #         print(point)
        # for every point in the rows shape attribute at the first element"
        for point in row[2].getPart(0):
            # Add 1 to your vertex ID number --- In other words increment the vertex id by 1"
            # Now we will write our rivers, including the id, vertex id, coordinates and the name of the river to the newly created text file!
            vertexId += 1
            print(point)
            # Add a line to your .txt file using the .write() method.
            # Each line should have five items, each separated by a space (manually
            # concatenated), and most of the items will need to be converted into
            # strings in the process (str() function). The five items are the OID,
            # vertex ID variable you created in the loop, the X-coordinate, the Y-coordinate,
            # and the name of the feature. Don't forget to add a "\n" at the end.
            # write the object  id number to the text file
            riversTxt.write(str(row[0]) + " ")
            riversTxt.write(str(vertexId) + " ")
            riversTxt.write(str(point.X) + " ")
            riversTxt.write(str(point.Y) + " ")
            riversTxt.write(row[1] + " ")
            riversTxt.write("\n")
            # You may want to also add a print statement that shows the same information
            # as is being written to the text file. This will also help to mark the
            # progress of your script, and identify errors.
print("\n")
print("All the rivers have been copied over from the rivers shapefile to the rivers text file! Awesome Work!")
## Step 4: Close the .txt file and delete row and cursor variables outside of all loops. ##
del cursor, row
riversTxt.close()