## tipovi podataka, start sa pythonom

string0 = 'Hello World'
print(string0)

int0 = 10
print(int0)

float0 = 10.2
print(float0)

bolean0 = True
print(bolean0)

character_a = 'a'
print(character_a)

complex_datatype = 1j
print(complex_datatype)

# to see the type of the variable
print(type(character_a))

# Declaring of multiple variables at once
a, b, c, d = 1, 'Stefan', 33.33, False
print(type(d))

"""String concatanation
print(string0 + int0) -it will NOT work"""

print("{} {}".format(string0, int0))

#f-Strings koristi se za konkatanaciju Stringova i za outpu gde imamo text + variabla

steps = 9200
name_runner = 'Test f-Strings'

print(f"{name_runner} walked {steps} steps\nStefan")

############################################

# Practice 1
print("#######################################################")

age = 25
height = 5.9
favorite_color = "blue"

print("Age:",age, "| Type:",type(age))
print("Height:",height, "| Type:",type(height))
print("Favorite Color:",favorite_color, "| Type:",type(favorite_color))

"""There are four collection data types in the Python programming language:
# 
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# Sequence type: list, tuple, range
# Mapping type: dict """


#TUPAL - ne mozes da menjas vrednost - immutable

tupal_one = ("apple", "banana", "cherry")
print(tupal_one[0])

#koliko se br 2 pronalazi puta u tupalu
print(tupal_one.count(2))
print(tupal_one.count("Stefan"))


# Lists - Arrays - mutable - mozes da ih edit kasnije

list_one = [1, "Stefan", 'S', True, 43.77]
print(list_one)

list_one.append("FANSTE")

print(list_one)

#duzina tj koliko entiteta postoji u listi
print(len(list_one))


# Dictionary

dict1 = {"key1": 1, "key2": 2, 3:"key3"}
print(dict1)
print("######################################################")
print(dict1["key1"])
print(dict1["key2"])
print(dict1[3])


# range - like a tupal just with range of numbers
x = range(6)
print(x)

# NoneType
x = None
print(x)