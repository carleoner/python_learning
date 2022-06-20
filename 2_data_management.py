
from email.quoprimime import quote

#########################
# string, int, float, complex (imaginary number)
#

name = "John"
age = 25
weight = 75.5
imaginary_number = 5 + 3j

print(imaginary_number)

##########################
# multi-line string
#

quote = """always
be
happy""" #multi-line string

print(quote)

##########################
# boolean
#

isLoggedIn = False

print(isLoggedIn)
print(5<10)

##########################
#  type()
#what type is it?

print(type(isLoggedIn))
print(type(quote))
print(type(imaginary_number))

##########################
# input()
#

username_age = input("Please enter your age:")
print(username_age)
print(type(username_age)) #input is a string value

#### conversion - int(), float(), complex(), bool()

username_age = int(input("Please enter your age:"))
print(username_age)
print(type(username_age)) #input is an int value