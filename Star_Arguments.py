# *args
def greet(*args):
    for name in args:
        print(f"Hello, {name}!")

# Calling the function with varying number of arguments
greet("Alice")
greet("Bob", "Charlie")
greet("Dave", "Eve", "Frank")

print('-'*10)
# **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with varying keyword arguments
print_info(name="Alice", age=30, city="New York")
print_info(name="Bob", profession="Engineer")
print_info()
