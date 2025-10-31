from center import Center
import utils

class Rectangle(Center):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        super().__init__(x, y)
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle(x={self._x}, y={self._y}, width={self._width}, height={self._height})"
    
    def __str__(self):
        return f"({self.x},{self.y}) represents the centerposition. The rectangles width is {self.width}, the hight is {self.height}"


    @property
    def width(self) -> int:
        return self._width
    
    @width.setter
    def width(self, value: int) -> None:
        utils.validate_type_number(value)
        utils.validation_positive_number(value)

        self._width = value

    @property
    def height(self) -> int:
        return self._height
    
    @height.setter
    def height(self, value: int) -> None:
        utils.validate_type_number(value)
        utils.validation_positive_number(value)

        self._height = value

    @property
    def area(self) -> float:
        return self.width*self.height
    
    @property
    def perimeter(self) -> float:
        return (self.width*2)+(self.height*2)
    
    def square(self) -> bool:
        if self.width == self.height:
            return True
        else:
            print("This is a rectangle, not a square")