# Write a program to create a class Parrot and perform the following tasks 
# 1- Create a class variable species 
# 2-Create a constructor that has instance variables - name and age
# 3-Create instances of class Parrot, passing arguments as well, P
#4- Print Class variable by accessing it, Print Instance variables as well
class parrot:
    species="Bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age

parr=parrot("Tom",5)
par2=parrot("Luca",15)
print(parr.name,"Is a",parr.species)
print(par2.name,"Is",par2.age," years old")