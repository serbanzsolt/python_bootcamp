
#? =============================================================================
#* 028 - OOP-Attributes and Classes
#? =============================================================================

"""
syntax:

class NameOfClass():

    def __init__(self,param1,param2):
        self.param1 = param1
        self.param2 = param2
        
    def some_method(self):
        #perform some action
        print(self.param1)
============================================================================        
'__init__' is the constructor of the class 
and it's called automatically when an object of the class created

'self' is represent the object itself

'self.param1 = param1' these are Attributes
we take in an argument and assign it using 'self.attribute_name'

"""

class Sample():
    pass

my_sample = Sample()
print(type(my_sample))

class Dog():
    def __init__(self, mybreed):
        self.breed = mybreed
        
my_dog = Dog(mybreed = "Huskie")
print(type(my_dog))
print(my_dog.breed)

# ==============================================================================
#* Dog class with more attributes
# ==============================================================================

class Dog2 ():
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        
        #expect Boolean T/F
        self.spots = spots
        
new_dog = Dog2(breed="Lab", name="Sammy", spots=False)
print(f"Attributes of the object: {new_dog.breed} {new_dog.name} {new_dog.spots}")