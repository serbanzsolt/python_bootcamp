# ==============================================================================
#* OOP - Coordinates: slope , distance
# ==============================================================================

class Line:
    
    def __init__(self, coor1: tuple, coor2: tuple):
        self.coor1 = coor1
        self.coor2 = coor2
        self.x1 = coor1[0]
        self.y1 = coor1[1]
        self.x2 = coor2[0]
        self.y2 = coor2[1]
        
    def __str__(self):
        #*Tuple UNPACKING!
        # x1,y1 = self.coor1
        
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        y2 = self.y2
        
        return f"This is a Line object. Point 1: ({x1},{y1}) point 2: ({x2},{y2})"
        
    def distance(self):
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        y2 = self.y2
        
        return (((x2-x1) ** 2) + ((y2-y1) ** 2)) ** 0.5
    
    def slope(self):
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        y2 = self.y2
        
        return (y2 - y1) / (x2 - x1)

cordinate1 = (3,2)
cordinate2 = (8,10)

my_line = Line(cordinate1, cordinate2)
print(my_line)
print(my_line.distance())
print(my_line.slope())