# #Pattern programme
# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print("\n")


#Invert pattern
# for i in range(6,1,-1):
#     for j in range(i,1,-1):
#         print("@",end=" ")
#     print("\n")

#Denomination calculator
total_amount=int(input("Enter your total amount: "))

lst_of_notes=[500,200,100,50,20,10,5,2,1]

for i in lst_of_notes:
    num_of_NOTES=total_amount//i
    total_amount=total_amount%i
    if num_of_NOTES!=0:
        print(f"The number of notes {i} is {num_of_NOTES}")