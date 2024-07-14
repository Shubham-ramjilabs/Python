def log(fun):
    def inner(*args,**kwards):
        result=fun(*args,**kwards)
        print(f"{fun.__name__} called ...result is {result}")
        return result
    return inner
@log
def add(a,b,c):
    return a+b+c
@log
def greet(name):
    return(f"Hello {name}")

print(add(1,2,3))
print(greet("Shubham"))

# add_wrapper=wrapper(add)
# print(add_wrapper(1,2,3))
# greet_wrapper=wrapper(greet)
# print(greet_wrapper("Shubham"))