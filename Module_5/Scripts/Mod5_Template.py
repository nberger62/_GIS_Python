####################################
## SCRIPT:      
## NAME:        
## CONTACT:     (email address)
## DATE:        
## DESCRIPTION:
##              
##              
####################################

## Step 1: Setup ##
    # import all modules and classes that you need, enable the overwriteOutput setting, set the workspace,
    # and define your feature class variable


## Step 2: Prepare to write .txt file ##
    # Create (open) a rivers.txt file for writing ("w"). See Assignment for syntax.

    # Create search cursor for rivers.shp. The cursor should call on the OID, SHAPE, and NAME fields.


## Step 3: Write to .txt file using for loops ##
    # Step 3a: First, iterate through each row/feature in the cursor/ShapeFile
        # Create a variable here to act as a vertex ID number.


    # Step 3b: Iterate through each point or vertex in the row. Remember to add the .getPart() method. 
        # Create for loop

        # Add 1 to your vertex ID number
        
        
        # Add a line to your .txt file using the .write() method. 
            # Each line should have five items, each separated by a space (manually
            # concatenated), and most of the items will need to be converted into
            # strings in the process (str() function). The five items are the OID, 
            # vertex ID variable you created in the loop, the X-coordinate, the Y-coordinate,
            # and the name of the feature. Don't forget to add a "\n" at the end.

        
            # You may want to also add a print statement that shows the same information
            # as is being written to the text file. This will also help to mark the
            # progress of your script, and identify errors.

            
## Step 4: Close the .txt file and delete row and cursor variables outside of all loops. ##


