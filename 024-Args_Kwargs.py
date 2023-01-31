
#? =============================================================================
#* 024 - *args and **kwargs (Arguments and KeyWord arguments)
#? =============================================================================

def myfunc (a,b,c=0):
    #Returns 5% of the sum of "a" and "b"
    return sum((a,b)) * 0.05

print("\nmyfunc:")
print(myfunc(40,60))

"""
def myfunc (a,b,c=0):
if we want to pass more parameters, but dont know how many we can use *args
"""
# ==============================================================================
#* Arbitrary number of arguments
#* ARGUMENTS return back TUPLE
# ==============================================================================

def myfunc2(*args):
    return sum(args)*0.05

print("\nmyfunc2:")
print(myfunc2(20,30,40,50,100,200))
print(myfunc2(11,2,4,2))

# ==============================================================================
#* Arbitrary number of keyword arguments
#* KEYWORD ARGUMENTS return back DICTIONARY
# ==============================================================================

def myfunc3(*args):
    for item in args:
        print(item)
print("\nmyfunc3:")
myfunc3(20,33,12,1,1000)

def myfunc4(**kwargs):
    if "fruit" in kwargs:
        print("My fruit of choice is {}".format(kwargs["fruit"]))
    else:
        print("I did not find any fruit")
        
myfunc4(fruit = "apple", veggie = "lettuce")

# ==============================================================================
#* *args and **kwargs in combination
# ==============================================================================

def combined (*args, **kwargs):
    print(args)
    print(kwargs)
    print("I would like {} {}".format(args[0],kwargs["food"]))

combined(10,20,30, fruit = "orange", food = "eggs" , animal = "fog" )