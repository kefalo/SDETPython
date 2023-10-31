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

################# 31. October 2023. #####################

x = int(input("Unesite jedan broj: "))
x1 = [1, 2, x]
print(x1[2])

l1 = ["Stefan", "Marinkovic", "QA Automation Eng", "SDET Python Selenium"]

print(l1[-1])

print(l1[1:3])
l1.insert(3, "insertTest")
print(l1)



#generating fibonaci
#a, b = 0, 1
#while a < 100:
#    print(a)
#    a, b = b, a+b