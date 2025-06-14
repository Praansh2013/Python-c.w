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

# Write a Python class named Rectangle with a length and width and a method that computes the area of a rectangle. Display the dimensions and calculated area of the rectangle as well
class rectangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        return self.l*self.w
    
    def p(self):
        return 2*(self.l+self.w)
l=int(input("Enter Length of the rectangle: "))
w=int(input("Enter Width of the rectangle: "))
r=rectangle(l,w)
print("Area of a rectangle with the length",r.l,"cm and a width of",r.w,"cm Is: ",r.area(),"cm square")
print("Perimeter of a rectangle with the length",r.l,"cm and a width of",r.w,"cm Is: ",r.p(),"cm")
