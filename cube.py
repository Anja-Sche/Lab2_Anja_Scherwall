from center import Center
import utils

class Cube(Center):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = side

    @property
    def side(self) -> int:
        return self._side
    
    @side.setter
    def side(self, value: int) -> None:
        utils.validate_type_number(value)
        utils.validation_positive_number(value)

        self._side = value

    @property
    def volume(self):
        return self._side * self._side * self._side
    
    @property
    def perimeter(self):
        return self._side * 12
    
    @property 
    def area(self):
        return (self._side * self._side) * 6
    
    def __repr__(self):
        return f"Cube(x={self._x}, y={self._y}, side={self._side})"
    
    def __str__(self):
        return f"({self._x}, {self._y}) represents the centerposition. The cubes sides are {self._side}"