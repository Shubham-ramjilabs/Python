name=input("Enter your name: ")
if len(name)<=5:
    raise Exception("Name should be greater than 5 characters")
print(f"Hello {name}")
