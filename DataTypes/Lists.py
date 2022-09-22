list1 = [1, 2, 4.5555, 'Stefan', "Jos jedna pobeda"]

print(list1[0]) #1

print(list1[2]) #4.5555

print(list1[-1]) #Jos jedna pobeda

print(list1[-2]) #Stefan

print(list1[2:5])


list1.insert(6, "Bravo")

print(list1)

print(list1[3:7])

list1.append('novo poglavlje')
print(list1[-1])


list1[6] = "NOVO POGLAVLJE"
print(list1[6])

print(list1)

del list1[1]

print(list1)