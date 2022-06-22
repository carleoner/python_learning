def sums(elem1, elem2):
    return elem1+elem2

def sayhi(name="user"):
    print(name)

print(sums(2,4))

sayhi()

####################
# lambda functions
add = lambda elem1,elem2: elem1 + elem2

print(add(5,6))