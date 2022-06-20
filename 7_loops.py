#############################
# range(start, stop, step{optional})


print(list(range(1,4,1)))

x = range(3, 6)
for n in x:
  print(n)

i=0
while i<3:
    if i==2:
        break
    else:
        print(f"i={i}")
    i+=1

some_str = "godfather"
for i in some_str:
    if i=='t':
        break
    else:
        print(i)
