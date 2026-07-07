def My_decor(func):
    def wrapper(a,b):
        print("start")
        return func(a,b)
    return wrapper
@My_decor
def add(a,b):
    return a+(b*10)
print(add(2,3))