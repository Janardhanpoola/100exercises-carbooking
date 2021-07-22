def decorator_func(original_func):
    def wrapper_func():
        return original_func()
    return wrapper_func

def display():
    print("this is display function")

res=decorator_func(display)
res()