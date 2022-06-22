#example
#dictionaries are unordered

dic1 = {1914: "WWI", 1939: "WWII", 1999: ["birth", "1 year to 2000"]}
print(dic1)

print(dic1[1939])
print(dic1.get(1999))

dic1[1939] = "WWIII"
print(dic1.get(1939))

dic1[2001] = "bd sis" # if key not present in dic it is added
print(dic1)

# deleting elements
del dic1[2001]

# dictionary functions

print(dic1.keys())
print(dic1.values())
print(dic1.items())
print(dic1.get(1939))
print(dic1.clear())
print(dic1.keys())

dic1.update({966:"chrzest", 1410:"grunwald"})
print(dic1.keys())

varDict = {"USA": ["PL", "IT", "FR"], "JAPAN":"CH"}
varDict["USA"].append("GR")
varDict["USA"].remove("IT")

print(varDict)

for i in varDict:
    print(i)

for i in varDict.values():
    print(i)

for i in varDict.items():
    print(i)