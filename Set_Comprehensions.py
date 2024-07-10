set={1,2,3,4,5}
sq=[x**2 for x in set]
print(sq)
# Create a set of squared numbers for even numbers only
even_squared_set = {x ** 2 for x in set if x % 2 == 0}
print(even_squared_set)  # Output: {4, 16}
# Create a set of unique characters from a string
sentence = "hello world"
unique_chars = {char for char in sentence if char != ' '}
print(unique_chars)  # Output: {'h', 'e', 'l', 'o', 'w', 'r', 'd'}
# Create a set of tuples (number, squared) for each number
tuple_set = {(x, x ** 2) for x in set}
print(tuple_set)  # Output: {(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)}
