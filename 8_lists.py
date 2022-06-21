#example

list1 = ["cat"]
list2 = ["John", 2, True]

list2[2] = False


print(list1)
print(list2[2])
print(list2[:1])

# delete elem from list
del list2[1]
print(list2)

# delete list
#del list2

# add elements in list
list3 = list1 + list2
print(list3)

# check if val is in the list
print("John" in list3)

# iteration 
print("\n")
for i in list3:
    print(i)

# check if part of list value is in the list
print("\n")
names = ["gefina", "ewa", "alina", "lucina", "ala"]
for i in names:
    if "ina" not in i:
        print(i)

# functions
# len(), min(), max()

print(len(list3))

list4 = [2,5,8]
print(min(list4))



# methods 
# append(elem), insert(index, elem), pop(), remove(elem), index(elem), count(elem)
list3.append(9)     #add at the end
print(list3.pop())  #remove and return last elem
print(list3)

even = [x for x in range(1,11) if x % 2 == 0]
print(even)