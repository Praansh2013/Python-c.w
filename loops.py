# # Write a Python program for printing the table of 17 (1 to 10), using for loop
# num=int(input("Enter a number and I will write its table "))
# for i in range(1,11):
#     print(num,"x",i,"=",num*i)

# Write a Python program for printing the sum of the first ten natural numbers using the while loop
j=1
sum=0
while j<11:
    sum=sum+j
    j=j+1
print("Sum=",sum)

# Write a Python program to take a number as input from the user and check whether it is a prime number or not
n=int(input("Enter a number: "))
flag=False
if n>1:
    for i in range(2,n):
        if n%i==0:
            flag=True
            break
if flag:
    print(n,"is not a prime number")
else:
    print(n,"is a prime number")