"""Formatting is nothing then using method format to pass the parameters which needs to be printed"""

name = "Stefan"
age = 31
sal = 3599.01

name, age, sal="Stef", 32, 100000

#Approach 1
print(name)
print(age)
print(sal)

print(name, age, sal)

#Approach 2
print("Ime je:", name)
print("Godine su:", age)
print("Plata je:", sal)

#Approach 3
print("Name is: %s , Age is:%d and Salary is: %g" % (name, age, sal))  # print the multiple variables by using temp variables %i


#Approach 4
print("Name is: {}, Salary is: {}, Age is: {}".format(name, age, sal))
