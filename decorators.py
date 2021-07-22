def lower_decorator(func):
    
    def wrapper():
        function=func()
        lower_case=function.lower()
        return lower_case
    
    return wrapper


def Capitalize_decorator(function):

    def wrapper():
        func=function()
        capital=func.capitalize()
        split_res="".join(capital.split())
        return split_res
    return wrapper


        
        




@lower_decorator
@Capitalize_decorator
def hello():
    return "Hello World"
    
print(hello())
    
        