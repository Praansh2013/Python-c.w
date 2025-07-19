file=open("demo.txt","r")
print(file.read())
file.close()

fw=open("demo.txt","w")
fw.write("This is a file write mode")
fw.write("Now you will see, this file is being overwritten")
fw.close()

fw=open("demo.txt","a")
fw.write("\nNow you will see, file will add new lines")
fw.close()

file=open("demo.txt","r")
print(file.read(14)) #this is used to read only some parts of file
print(file.readline())#this is used to print the first line of the file
print(file.readline())#if this is written multiple times, it will print multiple lines of the file
for x in file:
    print(x)#gives space after every line in the file
file.close()

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

#operations on a file 2
fi=open(r"C:\Users\defaultuser0\Downloads\Codingal.txt","r")
print(fi.read())
fi.close()
#write the file using with function
with open(r"C:\Users\defaultuser0\Downloads\Codingal.txt","w") as fil:
    fil.write("Hi! I am penguin from Codingal, and I am 1 year old")
#split the file into words
with open(r"C:\Users\defaultuser0\Downloads\Codingal.txt","r") as filee:
    data=filee.readlines()
    print("Words in this file are...")
    for line in data:
        word=line.split()
        print(word)

#create a new file
new_file=open("New_file.txt","x")
new_file.write("Hi! I am a penguin")
new_file.close()
#check if a file exists
import os
print("checking if my_file exists...")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")
#create a new if it does not
my_file=open("my_file.txt","w")
my_file.write("Hi,bye")
my_file.close()
#delete file named New file
os.remove("sample file.txt")
#delete the folder
os.rmdir("sample")