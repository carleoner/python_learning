
from turtle import pensize
from xml.sax.xmlreader import InputSource

"""
name = input("enter name:")
age = input("enter age:")

print("Hello {}. You are {} yo".format(name, age))
print("My name is {} {}".format("James", "Bond"))

##############################
# fstring

fname = input("enter fname: ")
print(f"Hello, {fname}")

##############################
# index in str

print(fname[0])
print(fname[1])

##############################
# slice that str
# [start:end:step] step is optional

print(fname[2:5])
print(fname[::2]) #print with step = 2

##############################
# negative index starts with -1
#  e x a m p l e
#  0 1 2 3 4 5 6
# -7-6-5-4-3-2-1

##############################
# str concentration
# str + str 
# join()

firstname = "Jakub"
lastname = "Zawadzki"
print(firstname + " " + lastname)
print(" ".join([firstname,lastname]))

print((firstname + " ")*5)

##############################
# str methods
# capitalize() - converts size of 1st char, count(x) - num of times val occurs, 
# find(x) - search for val in str - if true ret position, if false ret {-1}, 
# index(x)- search for val in str - if true ret index, if false ret execep (error),
# isalnum() - true if all char numeric, isalpha() - true if alphabet
"""

some_str = "Python_ex"
print(some_str.islower())
print(some_str.upper())
print(some_str.find("t"))
print(some_str.count("t"))
print(some_str.index("t"))
print(some_str.replace('P','A'))

# len(str)
print("length: " + str(len(some_str)))
print("length: {}".format(len(some_str)))
print(f"length: {len(some_str)}")
