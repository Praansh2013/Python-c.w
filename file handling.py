# file=open("demo.txt","r")
# print(file.read())
# file.close()

# fw=open("demo.txt","w")
# fw.write("This is a file write mode")
# fw.write("Now you will see, this file is being overwritten")
# fw.close()

# fw=open("demo.txt","a")
# fw.write("\nNow you will see, file will add new lines")
# fw.close()

# file=open("demo.txt","r")
# # print(file.read(14)) #this is used to read only some parts of file
# print(file.readline())#this is used to print the first line of the file
# print(file.readline())#if this is written multiple times, it will print multiple lines of the file
# for x in file:
#     print(x)#gives space after every line in the file
# file.close()

#program to remove lines starting with any prefix
file1=open("demo.txt","r")
file2=open("demoupdated.txt","w")
for line in file1.readlines():
    if not (line.startswith("This")):
        print(line)
    else:
        file2.write(line)
file1.close()
file2.close()