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
print(file.read())
file.close()