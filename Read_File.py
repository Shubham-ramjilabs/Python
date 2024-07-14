file_name="C:/Users/shubh/Desktop/facctum.txt"
file=open(file_name,"r")#open file in read mode
print(file.read())#read the file
print(file.readlines())#read the lines
print(file.readable())#check if the file is readable
print(file.writable())#check if the file is writable
print(file.closed)#check if the file is closed
print(file.close())#close the file