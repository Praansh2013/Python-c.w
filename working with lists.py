lst=["Apple", "Guava", "Mango","Banana","Kiwi"]
print(lst)
print("Length of list: ",len(lst))
print("First elemant: ",lst[0])
print("Last elemant: ",lst[-1])

lst.append("Papaya")
print("Upadated list: ",lst)

lst.remove("Guava")
print("Upadated list: ",lst)

lst.sort()
print("Sorted list: ",lst)

lst.pop()
print("Upadated list: ",lst)

lst.pop(1)
print("Upadated list: ",lst)

lst.reverse()
print("Reversed list: ",lst)

print("Double of list: ",lst*2)

lst=lst[0:4]
print("Sliced list: ",lst)

lst.clear()
print("Cleared list: ",lst)