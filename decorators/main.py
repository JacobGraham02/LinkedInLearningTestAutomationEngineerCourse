# A decorator is a function that takes another function and extends the behavior of this function without explicitly modifying it. This is a very powerful tool that allows you 
# to add new functionality to an existing function. 
'''
There are 2 types of decorators: Function and class decorators. A @ symbol preceeds a decorator
E.g. @my_decorator
def my_function():
    pass
    
Python has first class objects which can be defined inside another function, passed as an argument to another function, or returned from other functions.
Similarly, a decorator is a function that takes another function as an argument, wraps its behavior inside an inner function, and returns the wrapped function.



Function decorators:
Argument of function, wraps its behavior inside an inner function, and returns the wrapped function. 
def start_end_decorator(func):
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper
    
def print_name():
    print('Alex')
    
print_name()
print()

print_name = start_end_decorator(print_name)
print_name()
'''

def start_end_decorator(func):
    def wrapper():
        print('start')
        func()
        print('end')
    return wrapper

def print_name():
    print('Alex')
    

# Instead of wrapping our function and assigning it to itself, we can achieve the same by using a function decorator
@start_end_decorator
def print_name():
    print('Alex')

print_name()



# If our function has input arguments, we must call the function inside the wrapper with the arguments as well. Thus, we have to add *args and **kwargs to the inner function
def start_end_decorator_2(func):
    
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@start_end_decorator_2
def add_5(x):
    return x + 5

result = add_5(10)
print(result)