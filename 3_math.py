#arithmetic operations

# +,-,*,/,%,**,//
#

from enum import Flag


a=3
b=2
c=a+b

print("addition is:", c)
print("floor division:", a//b)

############################
# comparing stuff
# ==, !=, <, >, <=, >=

age = 16
required_age = 18
print("is an adult:", age > required_age)

#############################
# Logic op
# and, or, not

x = True
y = False

print("not x is:", not x)

############################
# membership

name = "any string"

print(" " in name)
print(" " not in name)

############################
# memory address

print(id(name))

############################
# identity operator

int1 = 4
int2 = 4
int3 = 5

print(int1 is int2) #true
print(int1 is int3) #false

############################
# walrus operator

print(name:="other string")