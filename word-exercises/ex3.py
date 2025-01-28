# Exercise 3:

# Importing sys library for user to be able to close the program.
import sys
from operator import itemgetter  # Importing item getter, which will be used in part E to make sorting easier.

print("Beginning Exercise 3...")

fileName = input("Enter the name of the file you wish to use: ") #Allowing the user to type a name of a file.

print("\n")

# Creating a function that searches the user's file for a player with a specific last name.
def tupleCreate(name):
    
    try:                               # Using try: and except: to catch potential error with the file name.
                                       #
        fileData = open(fileName, "r") # Reading the file given by the user,
                                       #
        line = fileData.read().split() # then, separating the lines gathered
                                       #
        dataTuple = (line)             # and putting them in a tuple.

        for i in dataTuple: # Using a for loop to iterate through the tuple.

            if name == i:

                tupleIndex = int(dataTuple.index(name)) # Calling an index() to find the position of the name, and using it as
                                                        # a reference point to reorder the items based on criteria of the exercise
                reqTuple = (dataTuple[tupleIndex], dataTuple[tupleIndex-1], dataTuple[tupleIndex+1], dataTuple[tupleIndex-2], dataTuple[tupleIndex-3]) 
        
                return reqTuple # Returning the newly rearranged tuple.
            
        fileData.close()
            
    except OSError as e: #If an error is caught, user is informed.

        print("You made a mistake in the name of the file, because there is no such file on your computer.")

        sys.exit() #Calling sys library to close the program.      

# Creating a function that works in a similar fashion as the one above,
# but instead creates a list of tuples containing the data provided inside the file:
def tupleAll():
    
    try:
        
        fileData = open(fileName, "r")

        line = fileData.read().split()

        dataTuple = (line)

        listAll = []

        tupleIndex = 2

        for i in range(0, len(dataTuple), 5): # Iterating through the length of the tuple containing all the items of the 
                                              # file in steps of 5, since it is known that each tuple must contain 5 items.
            reqTuple = (dataTuple[tupleIndex+1], dataTuple[tupleIndex], dataTuple[tupleIndex+2], dataTuple[tupleIndex-1], dataTuple[tupleIndex-2])

            listAll.append(reqTuple)    # Using the index of the first name in the tuple as a
                                        # reference point for arranging a new tuple, that mets requirements.
            tupleIndex += 5             # The index is then added with 5, since we know the next name comes after 5 items.
        
        return listAll                  # Returning the list of tuples.

        fileData.close()

    except OSError as e:

        print("You made a mistake in the name of the file, because there is no such file on your computer. Please restart.")

        sys.exit()

# Creating a function that returns the contents of a tuple as
# a string that is formatted based on the requirements of the exercise:
        
def tupleFormat(tupleName):

    tupleString = ", ".join(tupleName)

    return tupleString

# Creating a function that takes a tuple as an argument, and converts it into a list
# that will be used in the createTable() function:

def tablePrep(tupleName):

    returnList = [tupleName[0], tupleName[1], tupleName[2], tupleName[3], tupleName[4]]

    return returnList

# Creating a function that ensures every item that will be used for the table
# is equal to 15 characters, ensuring the table looks symmetrical:

def limitAdjust(string): # Taking a string that will be converted to have 15 characters using spaces.

    emptyString = ""

    space = " " # Defining the word "space" to refer to a space as a string character.
    
    while len(string) < 15: # Initiating a loop that will continue until the string is less than or equal to 15.

        space += " " # Every time the loop repeats, "space" will be given one more string space character.

        adjusted = space + string + space # Creating a new string that will be the input string with the spaces added.
        
        if len(adjusted) == 16: # Since spaces are added on both sides (2 characters) of the initial string, a condition is made
                               # so that if the string becomes 16 characters, a single space will be removed.
            newString = adjusted.replace(' ','',1)
            return newString
            break # Breaking the loop after adjusting the string
        
        if len(adjusted) == 15:

            return adjusted
            break # If the string is exactly 15 characters, the loop ends and returns the new string.

    if len(string) == 15: # If the string was already 15 chars, no changes are made.

        return string

# Creating a function that will use string
# characters to tabulate a list that it receives:

def createTable(tableList):

    # Creating the headers
    
    preset = ['Last Name','First Name','Salary','Position','Team'] # A preset list is defined, which will be used for headers.
    
    count = 0
    
    table = "" # Creating a string that will become a table.

    tableList.insert(0, preset) # The preset list above is inserted into the beginning of the list that the function receives.
    
    for item in tableList[0]:

        table += "|" + limitAdjust(item) # For every item that is in the list at the beginning of the larger tableList
                                         # a "|" character will be added as a separator, and added with the item within
    table += "|"                         # the list, which also goes through the limitAdjust() function, making it exactly 15 chars long.

    table += "\n"+("-")*(15*5)+("-"*6)   # A line is added to separate the headers. There will be 5 words that are 15 characters long, plus
                                         # 6 more "-" characters are added to account for each "|" character added above, making the table symmetrical.
    # Creating the rows:

    for item in tableList[1:]: # For each list that comes after the first "preset" list, a new line will be added.

        table += "\n"

        while count <= 4: # Creating a loop that will count from 0 to 4, going through all five items contained in a list within tableList
        
            table += "|" + limitAdjust(item[count]) # The items are structured the same way as the headers.

            if count == 4: # Once count reaches 4, that means all 5 items within a list have been formatted, so the count will reset,
                           # and break the 'while' loop, causing the for loop to go to the next list within tableList, and repeat the process
                count = 0  # for all lists within the large list.

                break

            count += 1
            
        table += "|"
    
    return table # Finally the function returns a string that contains the tabulated data.

# Main code:

listCheck = tupleAll() # Defining listCheck as a list created by the function tupleAll, which contains all the tuples created from the file.

removedList = []

count = 0

for content in listCheck:
    # Searching through the list for any lines that contain strings which do not meet 15 character or 8 digit requirements.
    if len(content[2].replace(',','')) > 8 or 15 < len(content[0]) or 15 < len(content[1]) or 15 < len(content[3]) or 15 < len(content[4]):

        removedList.append(content) # An empty list appends any content that meets the criteria above.

if removedList == []: # If the list is empty, that means all of the data gathered from the file did not contain more than 15 characters or 8 digits.

    table1 = []
  
    for content in listCheck: # The tuples are then converted to lists using tablePrep() function.

        table1.append(tablePrep(content))

    print(createTable(table1)) # Once the conversion is done, the lists are converted to a string that is tabulated and printed.

elif removedList != []: # If removedList contains something, that means the file contained
                        # words longer than 15 characters, or numbers longer than 8 digits.
    print("The following data was removed because either the individual strings in the file were longer than 15 characters, or player salaries contained more than 8 digits:","\n")

    table1 = []

    table2 = []
    
    for content in removedList:

        table1.append(tablePrep(content)) # The tuples that were appended by the removedList are prepped for tabulation.
        
        if content in listCheck: # Using a for loop to remove the tuples from the main list that the 'removedList' contained.

            listCheck.remove(content)
            
    print(createTable(table1)) # The tuples that were removed are then tabulated using functions.
    
    print("\n")

    print("Here is the new data that you can use: ","\n")
    
    for content in listCheck:

        table2.append(tablePrep(content)) # The main list containing tuples is then formated to have lists instead of tuples.

    print(createTable(table2)) # The data is tabulated.
        
print("\n")

# Preparing for option loop:
    
print("(A) If you wish to find out more about a player, type: 1")

print("(B) If you wish to find out more about players with a specific salary range, type: 2")

print("(C) If you wish to find out first and last names of all players within a team, type: 3")

print("(D) If you wish to find a player based on position and team, type: 4")

print("(E) If you wish to find a player based on position and lower and upper bounds of salary, type: 5")

print("(F) If you wish to add a player to the list, type: 6")

print("(G) If you wish to quit, type: 7","\n")

optionInput = input("Type your choice here: ")

print("\n")

# Entering the option loop based on user's input:

# Part A
if optionInput == "1":

    value = False # Setting a value wich will be used to check if the user made mistakes.
    
    userIn1 = input("Enter the player's last name you wish to find out about: ")

    funcList = listCheck # Calling the main list of tuples.
    
    for item in funcList:

        if userIn1 == item[0] or userIn1 == item[0].lower(): # Checking if the users typed in lased name matches any of the ones in the list of tuples.
                                                             # Also making sure that lower case is also accepted.
            print("\n","Here's the information:",tupleFormat(tupleCreate(item[0])))

            value = True # If a match is found, the data is printed and the value is set to true.
            
    if value is False: # If the value is still false, it means the user most likely made a mistake typing in the last name.

            print("\n","You either made a mistake in the name, or you entered a first name.") # The user is informed and the program stops.

            sys.exit()

# Part B
elif optionInput == "2":

    minVal = int(input("Enter the lower value of the salary: ")) # Getting the user's boundary numbers.

    maxVal = int(input("Enter the upper value of the salary: "))

    funcList = listCheck

    table1 = []

    playerInfo = []

    for item in funcList:

        if minVal <= int(item[2].replace(',','')) <= maxVal: # If there are salaries that fit the user's boundaries, the whole tuple containing
                                                             # the salary is appended to an empty list.
            playerInfo.append(item)

    if playerInfo != []: # If the list is not empty, that means there were items found that fit the boundaries.
    
        print("\n","Here is the information of players in your chosen salary range:","\n")

        for item in playerInfo:

            table1.append(tablePrep(item))

        print(createTable(table1)) # The data that is now tabulated, is printed to the user.
        
    elif playerInfo == []: # If the list is empty, that means no items were found that fit the user's defined boundaries. The user is then informed.

        print("There are no players in your chosen salary range.")

        sys.exit()

# Part C    
elif optionInput == "3":

    userTeam = input("Enter the team name: ") # Getting user input.

    funcList = listCheck

    nameList = []

    count = 0

    playerNames = []

    for item in funcList:

        if userTeam == item[4] or userTeam == item[4].lower(): # If the user input matches the team name contained in the list of tuples, the whole tuple is appended.
        
            nameList.append(item)
            
    if nameList != []: # If the list contains items, there were team names that matched the input.
        
        for item in nameList:

            playerNames.append(item[:2]) # Only the last and first names are appended from the tuples.

            count += 1 # Using "count" to count how many times this occurs.

        if count == 1: # If count += 1 occurs only once, that means there was only 
                       # one player found within the team, adjusting the grammar to be singular.
            print("There is",count,"player in",userTeam,":")

        else:

            print("There are",count,"players in",userTeam,":")

        count = 1
        
        for item in playerNames: # Printing the results of the search and formating them for better readability.

            print("Player",count,":","\n","First name:",item[1],"\n","Last name:",item[0])

            count += 1

    elif nameList == []: # If the list is empty, that means the user made a mistake, or the team did not have any players. Info is given.

        print("There are no players in",userTeam,". Or you just made a mistake in the name.")

        sys.exit()

# Part D
elif optionInput == "4":

    userPlayTeam = input("Enter the player's team: ")

    userPosition = input("Enter the player's position on the team: ")

    funcList = listCheck

    table1 = []

    playerList = []
    
    for item in funcList:

        if (userPlayTeam == item[4] or userPlayTeam == item[4].lower()) and (userPosition == item[3] or userPosition == item[3].lower()):
                                           # If any of the tuples within the list of tuples match both of the user's inputs
            playerList.append(item)        # the whole tuple containing the matching items is appended.

    if playerList == []: # Using the same way to check if mistakes were made by the user as above.

        print("No players were found in team",userPlayTeam,"with the position of",userPosition,".")
        
        sys.exit()

    elif playerList != []: # This means there were no mistakes, the program continues.

        print("\nHere's what was found: ","\n")
        
        for item in playerList:
            # The results are tabulated and printed using already defined functions:
            table1.append(tablePrep(item))

        print(createTable(table1))

# Part E    
elif optionInput == "5":

    userPosition = input("Enter a player's position: ") # Getting string input for the position of the player.

    minVal = int(input("Enter the lower bound of the salary range: ")) # Getting integer inputs for the boundaries.

    maxVal = int(input("Enter the upper bound of the salary range: "))

    funcList = listCheck

    processedList = []

    finalList = []

    tempList = []

    table1 = []

    for item in funcList:

        if (item[3] == userPosition or item[3].lower() == userPosition) and minVal <= int(item[2].replace(',','')) <= maxVal: # If any of the tuples fit both of the conditions
                                                                                                                              # they are then appended to an empty list.
            processedList.append(item)

    if processedList == []: # Checking for mistakes.

        print("There are no players that match all of your chosen categories.")
        
        sys.exit()

    elif processedList != []: # If no mistakes are made, program continues.

        for item in processedList:

            tupleAdjust = (item[0],item[1],int(item[2].replace(',','')),item[3],item[4]) # The salary within a tuple is converted
                                                                                         # from string to integer. The new tuple is         
            tempList.append(tupleAdjust)                                                 # appended to an empty list.
            
        tempList.sort(key=itemgetter(2)) # Using sort() function and an imported itemgetter function to sort the tuples 
                                         # within the list of tuples based on the salaries in an ascending order.
        for item in tempList:

            tupleAdjustStr = (item[0],item[1],"{:,}".format(item[2]),item[3],item[4]) # The integer salaries are now formatted
                                                                                      # with commas separating thousands.                          
            finalList.append(tupleAdjustStr)
                              
        print("Here are the results of players playing in",userPosition,"position, and with range of",minVal,"to",maxVal,". sorted in ascending order based on salary:","\n")
        
        for item in finalList:

            table1.append(tablePrep(item)) # The data is tabulated and printed using defined functions.

        print(createTable(table1))

# Part F        
elif optionInput == "6":

    # Getting the needed inputs from the user to add a new player to the list of tuples:
    lastName = input("Enter the player's last name (no more than 15 characters): ")
    
    firstName = input("Enter the player's first name (no more than 15 characters): ")

    salary = input("Enter the player's salary (use commas to separate thousands, no more than 8 digits): ")

    playPosition = input("Enter the player's position (no more than 15 characters): ")

    playTeam = input("Enter the player's team (no more than 15 characters): ")

    deleteCommas = salary.replace(',','') # Removing commas from the salary in order to check for length.

    table1 = []

    # Making sure that each of the inputs match the required criteria for the exercise.    
    if len(lastName) > 15:

        print(lastName,"has more than 15 characters. Please make sure the string you enter is no more than 15 characters, and restart.")

        sys.exit()
        
    elif len(firstName) > 15:

        print(firstName,"has more than 15 characters. Please make sure the string you enter is no more than 15 characters, and restart.")

        sys.exit()

    elif len(deleteCommas) > 8: # The salary without commas is tested for length.

        print(salary,"has more than 8 digits. Please make sure the number you enter is no more than 8 digits, and restart.")

        sys.exit()

    elif len(playPosition) > 15:

        print(playPosition,"has more than 15 characters. Please make sure the string you enter is no more than 15 characters, and restart.")

        sys.exit()

    elif len(playTeam) > 15:

        print(playTeam,"has more than 15 characters. Please make sure the string you enter is no more than 15 characters, and restart.")

        sys.exit()

    else: # If all of the inputs fit the criteria, the program continues.

        newTuple = (lastName, firstName, salary, playPosition, playTeam) # A new tuple with the player inputs is created.
        
        listNew = listCheck

        listNew.append(newTuple) # The tupple is added tu the list of tuples.

        for item in listNew:

            table1.append(tablePrep(item)) # The data is tabulated and printed:

        print("Here's the new table:\n")
        
        print(createTable(table1))

# Part G
elif optionInput == "7": # The program stops if the user requests it.

    print("Quitting... Goodbye!")

    sys.exit()

else: # If none of the "if" statements are used, that means the user entered an undefined input. The program quits.

    print("You probably entered something incorrect. Try again.") 

    sys.exit()
    
