
#? =============================================================================
#* 038 - Decorators
#? =============================================================================

def func():
    return 1

print(func)

def hello1():
    return "Hello!"

greet = hello1

print(greet())

del hello1
print(greet())
print("------------------------------------------------------------------------------")

def hello(name="Zsolt"):
    print("The hello() function has been executed!")
    
    def greet():
        return "\t This is the greet() function inside hello!"
    
    def welcome():
        return "\t This is welcome() function inside hello!"
    
    # print(greet())
    # print(welcome())
    # print("this is the end of the hello() function")
    
    print("I am going to return a function!!")
    
    if name == "Zsolt":
        return greet
    else:
        return welcome
    
hello()

my_new_function = hello("Zsolt")
print(my_new_function)
print(my_new_function())

def cool():
    
    def super_cool():
        return "I am very cool!"
    return super_cool

some_func = cool()
print(some_func())
print("------------------------------------------------------------------------------")

def hello():
    return "hi Zsolt"

def other(some_def_function):
    print("other code runs here!")
    print(some_def_function)
    
other(hello())
print("------------------------------------------------------------------------------")

def new_decorator(original_function):
    
    def wrap_func():
        
        print("Some extra code before the original function")
        
        original_function()
        
        print("Some extra code, after the original function")
        
    return wrap_func

def func_needs_decorator():
    print("I want to be decorated!")
    
func_needs_decorator()

decorated_func = new_decorator(func_needs_decorator)

decorated_func()
print()

@new_decorator
def func_needs_decorator():
    print("I want to be decorated!")
    
func_needs_decorator()