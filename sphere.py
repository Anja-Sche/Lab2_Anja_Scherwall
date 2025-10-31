from circle import Circle
import numpy as np

class Sphere(Circle):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    @property    
    def volume(self):
        return round(((self.radius**3)*np.pi*4)/3, 4)
    
    @property
    def circumference(self):
        return round(self.perimeter, 4)
        
    @property
    def area(self):
        return round((self.radius*self.radius)*np.pi*4, 4)
    
    def __repr__(self):
        return f"Sphere(x={self.x}, y={self.y}, radius={self.radius})"
    
    def __str__(self):
        return f"({self._x},{self._y}) represents the centerposition. The circles radius is {self.radius}"