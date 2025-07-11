import sys
def initial_phonebook():
    rows,cols=int(input("Enter initial number of contacts: ")),5
    phone_book=[]
    print(phone_book)
    for i in range(rows):
        print("\nEnter contact %d details in the following order (ONLY): "%(i+1))
        print("Note: * indicates mandatory fields")
        print("................................................................................")
        temp=[]
        for j in range(cols):
            if j==0:
                temp.append(str(input("Enter name*: ")))
                if temp[j]=="" or temp[j]==" ":
                    sys.exit("Name is a mandatory field. Process exiting due to blank field...")
            if j==1:
                temp.append(int(input("Enter number*: ")))  
            if j==2:
                temp.append(str(input("Enter an email id: ")))
                if temp[j]=="" or temp[j]==" ":
                    temp[j]==None
            if j==3:
                temp.append(str(input("Enter date of birth(dd/mm/yy): ")))
                if temp[j]=="" or temp[j]==" ":
                    temp[j]==None
        phone_book.append(temp)
        
    print(phone_book)
    return phone_book
def menu():
    print("................................................................................")
    print("\t\t\tSMARTPHONE DIRECTORY")
    print("................................................................................")
    print("\tYou can now perform the following operations on this phonebook\n")
    print("1) Add a new contact")
    print("2) Remove an exisisting contact")
    print("3) Delete all contacts")
    print("4) Search for a contact")
    print("5) Display all contacts")
    print("6) Exit phonebook")
    choice=int(input("Enter your choice"))
    return choice

def add_contact(pb):
    dip=[]
    for i in range(len(pb[0])):
        if i==0:
            dip.append(str(input("Enter name*: ")))
        if i==1:
            dip.append(int(input("Enter number*: ")))
        if i==2:
            dip.append(str(input("Enter email id: ")))
        if i==3:
            dip.append(str(input("Enter date of birth(dd/mm/yy): ")))
        if i==4:
            dip.append(str(input("Enter category(Family/Friends/Work/Others): ")))
    pb.append(dip)
    return pb
def remove_existing(pb):
    query=str(input("Enter the name of the contact you want to remove: "))
    temp=0
    for i in range(len(pb)):
        if query==pb[i][0]:
            temp+=1
            print(pb.pop(i))
            print("This contact has been removed")
            return pb
    if temp==0:
        print("Sorry, you have entered an invalid query.\nplease recheck and try again later.")
        return pb
def delete_all(pb):
    return pb.clear()

def search_existing(pb):
    choice=int(input("Enter search criteria \n\n\n 1) Name\n 2) Number\n 3)Email id\n 4) DOB\n 5) Category(Family/Friends/Work/Others)\n Please Enter: "))
    temp=[]
    check=-1
    if choice==1:
        query=str(input("Enter the name of the contact you want to search: "))
        for i in range(len(pb)):
            if query==pb[i][0]:
                check=i
                temp.append(pb[i])
    elif choice==2:
        query=int(input("Enter the number of the contact you want to search: "))
        for i in range(len(pb)):
            if query==pb[i][1]:
                check=i
                temp.append(pb[i])
    elif choice==3:
        query=str(input("Enter the email of the contact you want to search: "))
        for i in range(len(pb)):
            if query==pb[i][2]:
                check=i
                temp.append(pb[i])
    elif choice==4:
        query=str(input("Enter the DOB of the contact you want to search: "))
        for i in range(len(pb)):
            if query==pb[i][3]:
                check=i
                temp.append(pb[i])   
    elif choice==5:
        query=str(input("Enter the Category of the contact you want to search: "))
        for i in range(len(pb)):
            if query==pb[i][4]:
                check=i
                temp.append(pb[i])
    else:
        print("Invalid search")
        return -1
    if check==-1:
        return -1
    else:
        display_all(temp)
        return check
def dislpay_all(pb):
    if not pb:
        print("List is empty: []")
    else:
        for i in range(len(pb)):
            print(pb[i])
def thanks():
    print("................................................................................")
    print("Thank you for visiting our Smartphone directory system.")
    print("Please visit again!")
    print("................................................................................")
    sys.exit("Goodbye,have a nice day ahead!")

print("................................................................................")
print("Hello dear user, welcome to our smartphone directory system")
print("You may now proceed to explore this directory")

ch=1
pb=initial_phonebook()
while ch in (1,2,3,4,5):
    ch=menu()
    if ch==1:
        pb=add_contact(pb)
    elif ch==2:
        pb=remove_existing(pb)
    elif ch==3:
        pb=delete_all(pb)
    elif ch==4:
        d=search_existing(pb)
        if d==-1:
            print("The contact does not exist. Please try again")
    elif ch==5:
        dislpay_all(pb)
    else:
        thanks()