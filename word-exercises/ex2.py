#Exercise 2 part (a):

print("Beginning Exercise 2...")

#Importing the 'random' library which will be used for random number generation:
import random

#Defining empty lists which will be used for listGen function
list1 = []
list2 = []

#Defining the function that generates two lists filled with 15 random numbers between 100 and 0:
def listGen():

    #For loop that fills list1 with random numbersm and sorts it in ascending order:
    for i in range (0, 14):

        numRan = random.randint(0, 100)

        list1.append(numRan)

        list1.sort()

    #For loop that fills list2 with random numbersm and sorts it in ascending order:
    for n in range (0, 14):

        numRan = random.randint(0, 100)

        list2.append(numRan)

        list2.sort()

    #Combining the two lists into a new single list and then sorting it, and returning the result as a print command:
    list3 = list1 + list2

    list3.sort()

    return print(list3)

#Exercise 2 part (b):

#Defining the function that does conversions with the user's string input:
def stringCalc(text):

    #Using list() command to seperate the string into characters and the sorting it:
    listString = list(text)

    listString.sort()

    #Defining an empty string:
    textCon = ""

    #For loop that fills the empty textCon string with the values from listString:
    for i in listString:

        textCon += i

    return print(textCon)

#Exercise 2 part (c):

print("Beginning Exercise 2 part (c)...")

#Calling listGen() function that creates a combined sorted list of 30 total random numbers between 0 and 100:
listGen()

#Getting a string as input from the user:
userstr = input("Enter any word lower case letters: ")

#Calling stringCalc() function with the user's string
stringCalc(userstr)

print("Part (c) ended! Exercise 2 finished!")

