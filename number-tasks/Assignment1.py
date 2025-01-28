# Exercise 1
print("Beginning Exercise 1...")

# Function that calculates the length of number
def calc_number(n):
    calc = 0
    while n:
        n //= 10
        calc += 1
    return calc

#Function that checks if the number is narcissistic
def num_check(n):
    number1 = n
    total = 0
    num_dig = calc_number(n)
    while n:
        number = n % 10
        total += number ** num_dig
        n //= 10

    return total == number1

# Loop for printing narcissistic numbers
for i in range(1, 600000):
    if num_check(i):
        print(i)

print("Exercise 1 ended.")

# Exercise 2
print("Beginning Exercise 2...")

# Loop for finding primes in lines of 20
count = 0
for i in range(2, 1000):
    if i > 1:
        for y in range(2, i):
            if(i % y == 0):
                break
        else: # Adding code that prints 20 numbers per line
            count += 1
            print(i, sep=' ', end=(" " if count < 20 else "\n"))
            if count == 20:
                count = 0

print("Exercise 2 ended.")

# Exercise 3
print("Beginning Exercise 3...")

# Getting inputs from the user
num1 = int(input("Please enter your first positive integer: "))
num2 = int(input("PLease enter your second positive integer: "))

# Making a function calculating greatest common denominator
def denom(x, y):
    denom = 1
    if x % y == 0:
        return y
    for k in range(int(y/2), 0, -1):
        if x % k == 0 and y % k == 0: # Checking whether there is a remainder for both values, if not - it's the denominator
            denom = k
            break
    return denom

# Printing the greatest common divisor
print("The greatest common divisor of your two numbers is: ", denom(num1, num2))

print("Exercise 3 ended.")

# Exercise 4
print("Beginning Exercise 4...")

# Importing math for testing the accuracy of the taylor sereis loop, and for converting user's degree input into radians
import math

# Creating factorial function
def factorial(n):
    fctr = 1
    for i in range(2, n + 1):
        fctr *= i
    return fctr

# Getting user's input in degrees
user_value = math.radians(int(input("Enter your value in degrees: ")))

# Setting up the loop for calculating taylor series
fact_value = 0

for i in range(15):
    fact_value += ((-1)**i)*(user_value**(1+2*i))/factorial(1+2*i) # Taylor series loop for finding the sine of user input
    
print("The calculated sin value of your input is: ", fact_value)
print("Exercise 4 ended.")
print("Assignment finished!")
# Code used to test the accuracy of my results: print("The value using math lib is: ", math.sin(user_value))

    
