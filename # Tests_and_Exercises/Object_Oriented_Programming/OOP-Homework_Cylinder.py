# ==============================================================================
#* OOP - Cylinder
# ==============================================================================

class Cylinder:
    pi = 3.14
    
    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius
        self.base = (radius ** 2) * self.pi
        self.circumference = 2 * radius * self.pi
    
    def volume(self) -> float:
        # return (self.radius ** 2) * self.pi * self.height
        return self.base * self.height
    
    def surface_area(self) -> float:
        # return ((2 * (self.radius ** 2) * self.pi) + (2 * self.radius * self.pi * self.height))
        return (2* self.base) + (self.circumference * self.height)
    
    def __str__(self):
        return f"This is a Cylinder object. Height: {self.height}, Radius: {self.radius}"

c = Cylinder(2, 3)
print(c)
print(c.volume())
print(c.surface_area())