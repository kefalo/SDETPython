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
list_one = [False, 1, "Stefan", 'S', True, 43.77]
print(list_one)
print(list_one[-1])
print(list_one[2:4])
print(f"koliko puta {list_one.count('m')}")

#adding to the list
list_one.insert(3, "Marinkovic")
print(list_one)

list_one[2] = "STEFAN"  #updating the value for parameter
print(list_one)

list_one.append("FANSTE")
print(list_one)

del list_one[2:4]
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

dict2 = {}  #declaring empty dictionary, adding values later on the fly

dict2["key1"] = 1
dict2["key2"] = 2
dict2[3] = 3
print(dict2)

# range - like a tupal just with range of numbers
x = range(6)
print(x)

# NoneType
x = None
print(x)
