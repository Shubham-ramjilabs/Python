def palim(str):
    if len(str)<=1:
        print("Give String is Palindrom")
    else:
       if str[0]==str[-1]:
           palim(str[1:-1])
       else:
           print("Not Palindrom")

palim("add")          