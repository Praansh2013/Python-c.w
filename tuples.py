#empty tuple
tup=()
#tuples with data types
tup1=("Praansh",12,["Coding","Drawing"],("Bihar",))
print(tup1)
#display one item
print(tup1[2][1])
#updating tuple
tup2=list(tup1)
tup2[0]="Praansh Kapoor"
tup5=tuple(tup2)
print(tup5)
#Dictionaries
dict1={"Name":"Praansh","Age":12,"Gender":"Male","Hobbies":["Coding","Drawing"],"Grade":6}
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())
dict1["Age"]=11
print(dict1.popitem())
print(dict1)
dict1.pop("Age")
print(dict1)
print(dict1.clear())