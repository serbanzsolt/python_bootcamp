
#? =============================================================================
#* 030 - OOP - Inheritance and Polimorphism
#? =============================================================================

#* base Class

class Animal():
    
    def __init__(self):
        print("ANIMAL CREATED")
        
    def who_am_i(self):
        print("I am an animal")
        
    def eat(self):
        print("I am eating")
        
my_animal = Animal()

my_animal.who_am_i()
my_animal.eat()

# ==============================================================================
#* Making Dog class by inheritance of Animal class
# ==============================================================================

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("DOG CREATED")

    #* OVERWRITING BASE CLASS METHOD    
    def who_am_i(self):
        print("I am a Dog")
    
    #* new methods can also given
    def bark(self):
        print("WOOF!")

my_dog = Dog()

my_dog.who_am_i()
my_dog.eat()
my_dog.bark()
