# Step 5: Complete the comments section, below

##################################################
# Script name: Mod1_NBerger.py
# Author: Nathan Berger
# Email: nab45@students.uwf.edu
# Date: 5/18/2021
# Description:
##################################################


## Step 1 -> Print your last name from a created list

#### Step 1.1: Assign your full name, as a string, to a variable

stringName = "Nathan Alexander Berger"
print(stringName)

# Nathan Alexander Berger

#### Step 1.2: Split the string into individual names; assign list to variable

nameList = stringName.split(" ")
print(nameList)

# ['Nathan', 'Alexander', 'Berger']

#### Step 1.3: Using indexing, print your last name from the list

print(nameList[2])

# Berger

## Step 2 -> Fix established code for dice game

#### Step 2.1: Import the random module
import random

# list of player names
players = ['Tom', 'Jane', 'Phillip', 'Louis', 'Julius', 'Mary', 'Claudia', 'Marceline']

## Step 2.2: Correct the 2 errors in this loop
for p in players:
    x = len(p)
    dice = random.randint(0, x*2)
    print (p + " rolls a " + str(dice) + " out of " + str(x*2))
    if dice > x:
        print (p + " wins!")
    elif dice == x:
        print (p + " gets a tie.")
    else:
        print (p + " loses.")

# Tom rolls a 0 out of 6
# Tom loses.
# Jane rolls a 5 out of 8
# Jane wins!
# Phillip rolls a 10 out of 14
# Phillip wins!
# Louis rolls a 10 out of 10
# Louis wins!
# Julius rolls a 9 out of 12
# Julius wins!
# Mary rolls a 7 out of 8
# Mary wins!
# Claudia rolls a 1 out of 14
# Claudia loses.
# Marceline rolls a 18 out of 18
# Marceline wins!



## Step 3: Create a loop that adds 20 random numbers between 0 and 10 to a list.

#### Step 3.1: Create an empty list

randomNumbers = []

#### Step 3.2: Assign a counter variable 

counter = 0

#### Step 3.3: Create a while loop that appends a randomly generated number
####           between 0 and 10 into the list. Use an if and a break statement
####           to ensure the number of integers in the list doesn't exceed
####           twenty (20).

while True:
    randomNumbers.append(random.randint(0, 10))
    if len(randomNumbers) >= 20:
        break


#### Step 3.4: print list of 20 randomly generated integers

print(randomNumbers)

# [10, 7, 2, 3, 3, 0, 5, 10, 6, 10, 1, 9, 0, 1, 10, 10, 6, 4, 2, 8]

## Step 4: Create a loop that removes an unlucky number from the list generated
##         in step 3. 

#### Step 4.1: Assign a chosen integer to a variable

z = random.randint(0, 10)

#### Step 4.2: Use an if-else statement to determine whether the chosen integer
####           is listed in the previously created list from Step 3. If the int-
####           eger is not in the list, use a print statement to say so; if the
####           integer is in the list, use the count() method to identify how
####           identify how many times the integer exists within the list. Then
####           use a print statment to state how many times the number will be
####           removed from the list. You should have approximately 5 lines of code.
count = randomNumbers.count(z)
if count > 0:
    # count how many times z is in the list, then print the amount
    print("The number " + str(z) + " will be removed " + str(count) + " times")
else:
    # print it is not in the list
    print("Your number " + str(z) + " is not in the list!")

# EX: The number 6 will be removed 2 times

#### Step 4.3: Use a while loop and the remove() method to remove the unlucky
####           integer from the list created in Step 3.

while randomNumbers.count(z) > 0:
    randomNumbers.remove(z)


#### Step 4.4: Now use a print statement to print the updated list.

print(randomNumbers)

# Ex: [0, 0, 10, 0, 7, 2, 0, 4, 8, 0, 10, 5, 9, 10, 5, 9, 1, 2, 7]