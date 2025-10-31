from center import Center
import numpy as np
import utils

class Circle(Center):
    def __init__(self, x= 0, y= 0, radius = 0) -> None: #place radius first for no default value??
        super().__init__(x, y)
        self.radius = radius

        self._area = 0
        self._parimeter = 0

    def __repr__(self):
        return f"Circle(x={self._x}, y={self._y}, radius={self.radius})"
    
    def __str__(self):
        return f"({self._x},{self._y}) represents the centerposition. The circles radius is {self.radius}"


    @property
    def radius(self) -> int:
        return self._radius
    
    @radius.setter
    def radius(self, value: int) -> None:
        utils.validate_type_number(value)
        utils.validation_positive_number(value)

        self._radius = value
    
    @property
    def area(self) -> float:
        return (self.radius*self.radius)*np.pi
    #fix float?
    
    @property
    def perimeter(self) -> float:
        return (self.radius + self.radius)*np.pi
    #fix float?

    def unit_circle(self) -> bool:
        if self.x == 0 and self.y == 0 and self.radius == 1:
            return True
        else:
            return False