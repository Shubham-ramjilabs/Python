
def cache(fun):
    print("initializing cache")
    cache={}
    def inner(*argss):
        if argss in cache:
            print("cache hit")
            return cache[argss]
        else:
            print("cache miss")
            result=fun(*argss)
            cache[argss]=result
            return result
    return inner


@cache
def add(a,b):
    return a+b

print(add(1,2))

print(add(1,2))

