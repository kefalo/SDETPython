# inputs are always parsed as String variable / in order to use input we need to convert
input("Enter number")

input1 = input("enter n1: ")
input2 = input("enter n2: ")

# printing the actual type of input from user

print(type(input1))
print(type(input2))

print(input1 + input2)


# Approach 1 - getting the input from user as int value
inputAsNumber = int(input("Enter first number: "))
inputAsNumber2 = int(input("Enter second number: "))

print(inputAsNumber, inputAsNumber2)

# addition operation over two inputs
print(inputAsNumber + inputAsNumber2)

# Approach 2 - getting the data as string format, then conversion of String at the place we need

num1 = input("Enter first num1: ")
num2 = input("Enter first num2: ")

print(int(num1) + int(num2))


# Example with float - var = type(input("Pls Enter you Input"))

decimal1 = float(input("Enter decimal number:"))
decimal2 = float(input("Enter second decimal number:"))
print(decimal1, decimal2)
decTotal = decimal1 + decimal2
print(decTotal)

