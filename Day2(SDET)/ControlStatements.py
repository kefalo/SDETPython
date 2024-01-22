"""
Conditional Statements:
if, if..else, elif

Looping Statements:
while, for

Jumping Statements:
break, continue
"""

# Conditional Statements

# Example1

age = int(input("How old are you? Enter the number of years:"))

if age >= 18:
    print("Eligible for vote")
else:
    print("Persona not eligible for vote")
print(age)


# Example 2

if False:
    print("true")
else:
    print("false")


# Example 3
if 0:
    print("one, means 'True'")
else:
    print("not one(true), it's '0'(false)")

# Example 4 : Find if a number is a even number or not

num = int(input("Enter the number "))

if num % 2 == 0:
    print("Number is even")
else:
    print("Number is not even")

# Example 5 - if else in single line (ternary operator)
num1 = float(input("Unjesite unjeseno"))

print("Jednacina nejednacine resena na pozitivicu") if num1 % 2 == 0 else print("jebes ga nije fer not 'even'")

