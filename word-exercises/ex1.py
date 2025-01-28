#Exercise 1 part (a)

#Defining a function that checks if the two words are palindromes by reversing:

def checkPalin(s1, s2):
    
    if s1 == s1[::-1] and s2 == s2[::-1]:
        
        value = True
        return value
    
    elif s1 != s1[::-1] and s2 == s2[::-1]:
        
        value = "s1"
        return value
    
    elif s2 != s2[::-1] and s1 == s1[::-1]:
        
        value = "s2"
        return value
    
    else:
        
        value = False
        return value
    
#Exercise 1 part (b)

#Defining a function that checks if the user's sentence is a palindrome
    
def checkPalinSen(sen1):
    
    proc = sen1.lower().strip().replace(" ","")
    
    if proc == proc[::-1]:
        
        value1 = True
        return value1
    
    else:
        
        value1 = False
        return value1

#Exercise 1 part (c):

print("Beginning part (c)...")

#Getting the two words as strings from the user

word1 = str(input("Enter your first word: "))
word2 = str(input("Enter your second word: "))

#Checking for palindromes and providing the user with information on which words are palindromes or not

if checkPalin(word1, word2) is True:
    
    print("True.",word1,"is the same backwards. This is also true for",word2,".")
    
elif checkPalin(word1, word2) == "s1":
    
    print("False.",word1,"is not a palindrome, but",word2,"is a palindrome.")
    
elif checkPalin(word1, word2) == "s2":
    
    print("False.",word2,"is not a palindrome, but",word1,"is a palindrome.")
    
elif checkPalin(word1, word2) is False:
    
    print("False. Both",word1,"and",word2,"are not palindromes.")

#Getting the sentence as a string from the user

sentence = input("Type your sentence here: ")

#Checking if the sentence is a palindrome or not

if checkPalinSen(sentence) is True:
    
    print("True.'",sentence,"' is a palindrome.")
    
elif checkPalinSen(sentence) is False:
    
    print("False.'",sentence,"' is not a palindrome.")

print("Part (c) ended. Exercise 1 finished!")
