def angle(h,m):
    minuteangle=6*m

    hourangle=30*(h%12)+m*0.5
    angle=minuteangle-hourangle
    return angle



h=int(input("Enter the hour"))
m=int(input("Enter the minute"))

print(angle(h,m))