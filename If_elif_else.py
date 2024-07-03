mark=int(input("Enter your mark: "))
if mark<40:
    print("Fail")
elif mark<50:
    print("Pass")
elif mark<60:   
    print("Second class")
elif mark<70:
    print("First class")
elif mark<80:
    print("Distinction")
else:
    print("Excellent")