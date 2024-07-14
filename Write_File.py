file_name="C:/Users/shubh/Desktop/facctum.txt"
with open(file_name,"r") as file:
    data=file.readlines()

file_name=("C:/Users/shubh/Desktop/writefile.txt")
with open(file_name,"w") as file:
    for i in data:
        file.write(i)

with open(file_name,"r") as file:
    print(file.read())