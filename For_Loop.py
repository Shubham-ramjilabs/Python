# l=[1,2,3]
# #fech the iterator
# iter_num=iter(l)
# print(iter_num)

# #using next function print the value
# print(next(iter_num))
# print(next(iter_num))
# print(next(iter_num))

#we can cerate out for loop

def for_loop(iterable):
    iterator=iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

l=[1,2,3,4,5]
for_loop(l)
l1={1,2,3,4,5,60}
for_loop(l1)

