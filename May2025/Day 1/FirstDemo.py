print("Hello World")

int = 10
n = 11.11
s = "String"
c = 'C'

d, g, h, j = 1, 6.7, 'chao', 's'

print(type(int))
print(type(n))
print(type(s))
print(type(c))


# When there is no concatanation - in cases when we try to concatanate two different value types - not possible - only with same data type
print("{} {}".format("Value is", int))
print(type(h))

#liste
listaInt = [1,2,3,4,5]
listaFloat = [1.1,2.2,3.3,4.4,5.5]
listaChar = ['A', 'B', 'C', 'D']

lista1 = [1, 2, 3, "Stefan", "Marinkovic"]

print(lista1[3:4])

lista1.insert(5, "Bravo")
print(lista1[5])
print("{} {}".format(listaInt, listaFloat))