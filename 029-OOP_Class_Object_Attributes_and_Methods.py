
#? =============================================================================
#* 029 - Class object attributes and methods
#? =============================================================================

class Dog():
    # Here are the class object attributes
    # These ones are same for every instance of the class
    species = "mammal"
        
    def __init__(self, breed, name, spots):
        
        self.breed = breed
        self.name = name
        self.spots = spots
        
    # OPERATIONS / Actions ----> METHODS
    #* METHOD is a function inside a class working with the object someway
    def bark(self):
        print(f"WOOF! my name is {self.name}")
        
my_dog = Dog(breed="Lab", name="Sammy", spots="False")
print(f"Attributes: {my_dog.breed}, {my_dog.name}, {my_dog.spots} and the class object one is: {my_dog.species}")
my_dog.bark()
print(my_dog.bark)

# ==============================================================================
#* next class
# ==============================================================================

class Circle():
    #class object attribute
    pi = 3.14
    
    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius ** 2 * self.pi
    
    def get_circumference(self):
        return 2 * self.radius * self.pi
    
my_circle = Circle(25)
print(my_circle.get_circumference())
print(my_circle.area)