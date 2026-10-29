"""
Working with Lists
Create a list named fruits that contains below five different fruit names (strings).

"apple", "banana", "cherry", "date", "elderberry"
Print the first and last elements of the list.

Use slicing to print the second and third fruits from the list.

Expected Result:

First fruit: apple
Last fruit: elderberry
Fruits from index 1 to 2: ['banana', 'cherry']

"""
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Fruits from index 1 to 2: {fruits[1:3]}")


############### Tuples ###############
"""
Exploring Tuples
Create a tuple named person that contains three elements: a name (string), an age (integer), and a height (float) with the below values.
"Rahul", 25, 5.9

Print the second element of the tuple.

Expected Result:
Age: 25
"""
person = ("Rahul", 25, 5.9)

print(f"Age: {person[1]}")




################ Dictionary ###################
"""
Understanding Dictionaries
Create a dictionary named car with the following keys: make, model, year, and color. Assign appropriate values to each key.

    "make": "Toyota",

    "model": "Camry",

    "year": 2020,

    "color": "Blue"

Print the value associated with the model key.

Add a new key called owner and assign it the name "Rahul".

Print the entire dictionary.

Expected Result:
Car model: Camry
Updated car dictionary: {'make': 'Toyota', 'model': 'Camry', 'year': 2020, 'color': 'Blue', 'owner': 'Rahul'}
"""

car = {"make":"Toyota", "model":"Camry", "year":2020, "color":"Blue"}
print(f"Car model: {car['model']}")

car["owner"] = "Rahul"

print(f"Updated car dictionary: {car}")