
#? =============================================================================
#* 032 - OOP Abstract class
#? =============================================================================

# ==============================================================================
#* More common way then polimorphism is: to use Abstract class and Inheritance
#* Abstract class shoudn't be instatiated, it should be used as a Base class
#* Only for Inheritance
# ==============================================================================

class Animal():
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        raise NotImplementedError ("Subclass must implement this abstract method")

#* Generate an error
# my_animal = Animal("fred")
# my_animal.speak()

class Dog(Animal):
    
    def speak(self):
        return self.name + " says WOOF!"
    
class Cat(Animal):
    
    def speak(self):
        return self.name + " says MEOW!"
    
fido = Dog("Fido")
isis = Cat("Isis")

print(fido.speak())
print(isis.speak())