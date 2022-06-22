
# sets are unordered
# CANNOt access individual elements 

data = set() #empty set

set1 = {2, 5.6, "Pete"}
print(set1)
print(type(set1))

for i in set1:
    print(i)


##########################
A = {1,2,3,4,5,6}
B = {2,5,7,6,8,9}

print(A|B)
print(A.union(B))

print(A&B)
print(A.intersection(B))

print(A - B)
print(A.difference(B))
print(B - A)
print(B.difference(A))

print("sorted set B", sorted(B))
print("length set B:", len(B))
print("max in set B:", max(B))
print("sum in set B:", sum(B))

set1.discard(5.6) #removes elem from the set if member
set2 = set1.copy() #returns copy of set
set2.add(55) #add elem to set

print(set2)