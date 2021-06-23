####################################
# SCRIPT: Mod6A_NAB.py
# NAME: Nathan Alexander Berger
# CONTACT: nab45@students.uwf.edu
# DATE: 6/19/2021
# DESCRIPTION: This script is a python script in ArcPY in which we are creating a new GDB to save a new raster file, and the new raster will have the following attributes...
# Forest landcover classifications: 41, 42, and 43
# Slope between: 5° and 20°
# Aspect between: 150° and 270°
# This script should only run if the spatial analyst extension is available. Once we run all of our slope, aspect, and landcover classification calculations, we will then combine
# all our raster files (5 total) intro one large raster file. We will save this new raster to our new GDB and check the raster file in Arc Pro to make sure it is correct.
# If someone does not have the spatial analyst extension, we will make sure that this script prevents them from running this processing and return a print statement saying that the extension is not available
####################################

### Step 1: Setup ###
    # import arcpy module, env class, and Spatial Analyst module
import arcpy
from arcpy import env
from arcpy.sa import *
print("Seeting up my script by importing my modules " + "\n")


    # enable overwriteOutput
env.overwriteOutput = True
print("Enabling overwrite output to true! " + "\n")

    # Set workspace to Elevation.gdb that contains your elevation and landcover rasters
    # A later step seems to require that you work from a gdb, and not from a folder
env.workspace = "C:/Users/Admin/PycharmProjects/UWF/Module_6/Data/Mod6_Data/Elevation.gdb"
print("Setting up my workspace " + "\n")

# Get and print a list of GRIDs from the workspace
rasters = arcpy.ListRasters()
for raster in rasters:
    print(raster)
    desc = arcpy.Describe(raster)
    print("Raster spatial reference is: " + desc.spatialReference.name)
    print("Raster format is: " + desc.format)
    print("Raster compression type is: " + desc.compressionType)
    print("Raster number of bands is: " + str(desc.bandCount))
    print("\n")

### Step 2: Optional -- Create new GDB ###
    # Create new gdb for your output raster (Only required if final output is in GRID format.
    # If not saving to gdb, must give final output a file extension, such as .tif.)
print("Creating a new GDB to save our output raster later on in our script!")
arcpy.CreateFileGDB_management("C:/Users/Admin/PycharmProjects/UWF/Module_6/Output", "rasters.gdb")
print(arcpy.GetMessages() + "\n")
print("************************************************************************************")

### Step 3: Create new raster ###
    ## Step 3a: Make sure spatial analyst is available ##
        # Create conditional statement so that the code only runs if the spatial analyst
        # extension is available
if arcpy.CheckExtension("spatial") == "Available":
    ## Step 3b: Check out the spatial analyst extension ##
    arcpy.CheckOutExtension("spatial")
    # do a test function using the spatial analyst extension
    outraster = arcpy.sa.Slope("elevation", "PERCENT_RISE")
    outraster.save("C:/Users/Admin/PycharmProjects/UWF/Module_6/Output/slope_per")
    print(arcpy.GetMessages() + "\n")

## Step 3c: Isolate the forest
    # Use the RemapValue function to assign landcover classifications 41, 42 and 43
    # all as new value of 1
    print("Setting the remap value to assign our new landcover classifications!" + "\n")
    myRemapVal = RemapRange([[41, 1], [42, 2], [43, 3]])

    # myremap = RemapValue([[41, 1], [42, 2], [43, 3]])

    # Use the Reclassify tool on the landcover raster, using the RemapValue variable
    landreclass = Reclassify("landcover", "VALUE", myRemapVal, "NODATA")
    landreclass.save("C:/Users/Admin/PycharmProjects/UWF/Module_6/Output/reclassland")
    print(arcpy.GetMessages())

## Step 3d: Prepare for slope and aspect calculations ##
    # Assign the elevation raster to a variable using the .Raster function
    print("Assigning the elevation raster to a varibale... " + "\n")
    elevraster = arcpy.Raster("elevation")
    outelevraster = elevraster * 3.281
    outelevraster.save("C:/Users/Admin/PycharmProjects/UWF/Module_6/Output/elev_good")

    # Create variables for slope and aspect, using the .Slope and .Aspect functions
    # on the elevation raster variable
    print("Creating the variables for Slope and Aspect! " + "\n")
    slope = Slope(outelevraster)
    aspect = Aspect(outelevraster)
    print(arcpy.GetMessages())

## Step 3e: Perform slope and aspect calculations ##
    # Create temp variables for all conditions. If final value must be between two values,
    # two temp variables are needed: one greater than low value, one less than high value
    print("Performing the slope and aspect calculations! " + "\n")
    lowSlope = slope > 5
    highSlope = slope < 20
    # finalSlope = lowSlope & highSlope
    lowAspect = aspect > 150
    highAspect = aspect > 270
    # finalAspect = lowAspect & highAspect

## Step 3f: Combine all five temporary rasters ##
    # Combine all five temp rasters into one final raster,
    # using ampersands (Boolean And map algebra operator)
    print("Now we will combine all 5 rasters together!")
    # the four slope & aspect rasters and the reclassified landcover from step 3c
    finalResults = highAspect & highSlope & landreclass & lowAspect & lowSlope


## Step 3g: Save the final raster ##
    # use the .save function to save the combined raster. If saving to a GDB, do not use
    # a file extension. If saving to a folder, a file extension will be required (e.g. .tif)
    print("Save the final raster as a permanet raster file in our new GDB!" + "\n")
    finalResults.save("C:/Users/Admin/PycharmProjects/UWF/Module_6/Output/rasters.gdb/final")
    print(arcpy.GetMessages())
## Step 3h: Check in the spatial extension ##
    arcpy.CheckInExtension("spatial")

### Step 4: If spatial analyst is not available... ###
    ## Create else condition that prints a message if the spatial analyst extension is not available
else:
    print("Spatial Analyst license is not available...")