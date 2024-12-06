# Practice variables - Lecture 9
name = "Jack"
print(name)

name = "Jasmine"
print(name)


print(len(input("What is your name, we will tell you how much characters it has")))
# small practice, breaking above line into readable code and use practice
username = input("What is your username? ")
length = len(username)
print(length)


#Practice
# Variables
# We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice.
# Write 3 lines of code to switch the contents of the variables.
# You are not allowed to type the words "milk" or "juice".
# You are only allowed to use variables to solve this exercise.


glass1 = "milk"
glass2 = "juice"

#use a temp variable to store the value before the change(Swap)
#tempGlass1 = glass1
#glass1 = glass2
#glass2 = tempGlass1

#or shorter version of integrated python construct

glass1, glass2 = glass2, glass1

# Addition and Subtraction
x = x + y
y = x - y
x = x - y

# Multiplication and Division
x = x * y
y = x / y
x = x / y

# XOR swap
#
# This algorithm works for integers only
x = x ^ y
y = x ^ y
x = x ^ y

# Python String swapcase

name = "JoHn CeNa"

# converts lowercase to uppercase and vice versa
print(name.swapcase())

# Output: jOhN cEnA

# Variable Naming - Lecture 10

#naming the variable,
user_name = "JoHn CeNa"
number1 = 1
