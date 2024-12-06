# Practice 1 for Print

str1 = "1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl."
str2 = "2. Knead the dough for 10 minutes."
str3 = "3. Add 3g of Salt."
str4 = "4. Leave to rise for 2 hours."
str5 = "5. Bake at 200 degrees C for 30 minutes."


print(str1)
print(str2)
print(str3)
print(str4)
print(str5)


# Strings manipulation
# separate line manipulation
print("Text and there is some text i will write in next line,\nand this is the part in next line,\nand there is another one")

# string concatenation
print("hello " + "world" + " 369")
print("hello " + str(123))

# Practice2

# Fix the code below 👇

print("Notes from Day 1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("String Concatenation is done with the + sign")
print("New lines can be created with a \ and the letter n")


# Practice 3 - printing and using input function to actually do a input from a command line
print("What is your name?")

input("What is your name?(input)")

print("Hello " + input("What is your name?") + '!') ##also right for the practice 4, I did it good and before the video lecture

# Practice 4(lecture 8) - fix the issue, use all what learned and fix the issue - I've done it on the other way, by defining variable for the input
str1 = input("What is your name?")
print("Hello " + str1 + '!')