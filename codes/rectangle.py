from center import Center
from utils import validate_type_number
from utils import validation_positive_number

class Rectangle(Center):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        super().__init__(x, y)
        self.width = width
        self.height = height

        self._area = 0
        self._parimeter = 0

    def __repr__(self):
        return f"Rectangle(x={self._x}, y={self._y}, width={self._width}, height={self._height})"
    
    def __str__(self):
        return f"({self.x},{self.y}) represents the centerposition. The rectangles width is {self.width}, the hight is {self.height}"


    @property
    def width(self) -> int:
        return self._width
    
    @width.setter
    def width(self, value: int) -> None:
        validate_type_number(value)
        validation_positive_number(value)

        self._width = value

    @property
    def height(self) -> int:
        return self._height
    
    @height.setter
    def height(self, value: int) -> None:
        validate_type_number(value)
        validation_positive_number(value)

        self._height = value

    @property
    def area(self) -> float:
        area = self.width*self.height
        self._area = area
        return self._area
    
    @property
    def perimeter(self) -> float:
        perimeter = (self.width*2)+(self.height*2)
        self._perimeter = perimeter
        return self._perimeter 
    
    def square(self) -> bool:
        if self.width == self.height:
            return True
        else:
            print("This is a rectangle, not a square")