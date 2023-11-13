# a=10
# b=20
# s='welcome'
#
# print(type(a))
# print(type(b))
# print(type(s))


### Example 1 ### single line print for multiple variables

a=10.5
b=12.8
# print(a)
# print(b)

print(a,b)

### Example 2 ### single statement for declaring multiple variables, printing them ##

a=10.5
b=12.8
c='welcome'
a,b,c = 11,25,'dva broja'
print(a,b,c)


### Example 3 ### - if values are same for all variables, use equals
a=100
b=100
c=100

a=b=c=100

print(a,b,c)


### Example 4 ### - swaping of the values

x=1
y=2
print(x,y)

y,x = x,y

print(x,y)