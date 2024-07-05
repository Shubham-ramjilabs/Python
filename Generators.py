def my_generator():
    for i in range(5):
        yield i

gen=my_generator()
#1 way to print
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#2 way to print
for j in gen:
    print(j)