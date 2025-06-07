def ab(n):
    if n>0:
        return n
    else:
        return -n
n=int(input("Enter a number here, I will write its absolute value: "))
a=ab(n)
print("The absolute value of",n,"is",a)