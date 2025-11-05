from center import Center
import utils

class Rectangle(Center):
    """
    A class representing the shape rectangle.

    Attributes:
    - x (int): The coordinate on the x axel.
    - y (int): The coordinate on the y axel.
    - width (int): The width of the rectangle.
    - height (int): The height of the rectangle.

    Operators:
    - operators for comparison: ==, <, <=, >, >= 

    Methods:
    - translate(): Moves the center position by adding to the existing one.
    - square(): Checks if the figure is a square or not.

    Example usage:
    >>> rectangle1 = Rectangle(2, 2, 3, 1)
    >>> rectangle1.square()
    This is a rectangle, not a square
    >>> rectangle1.translate(-1, 2)
    >>> rectangle1
    Rectangle(x=1, y=4, width=3, height=1)
    """

    def __init__(self, x:int|float=0, y:int|float=0, width: int|float=1, height: int|float=1) -> None:
        """
        Initializes an new instance of the class Rectangle.

        Parameters:
        - x (int): The coordinate on the x axel.
        - y (int): The coordinate on the y axel.
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        """
        super().__init__(x, y)
        self.width = width
        self.height = height

    @property
    def width(self) -> int|float:
        return self._width
    
    @width.setter
    def width(self, value: int|float) -> None:
        utils.validate_type_number(value)
        utils.validation_positive_number(value)

        self._width = value

    @property
    def height(self) -> int|float:
        return self._height
    
    @height.setter
    def height(self, value: int|float) -> None:
        utils.validate_type_number(value)
        utils.validation_positive_number(value)

        self._height = value

    @property
    def area(self) -> float:
        return round(self.width*self.height,4)
    
    @property
    def perimeter(self) -> float:
        return round((self.width*2)+(self.height*2),4)
    
    def square(self) -> bool:
        """Checks if the figure is a square or not."""
        if self.width == self.height:
            return True
        else:
            print("This is a rectangle, not a square")

    
    def _left_corner_position(self) -> tuple:
        """Calculates the left corner of the rectangle. Used when class Shape2dPlotter"""
        x_position = self._x - (self._width/2)
        y_position = self._y - (self._height/2)
        return (x_position, y_position)
    
    def __repr__(self) ->str:
        return f"Rectangle(x={self._x}, y={self._y}, width={self._width}, height={self._height})"
    
    def __str__(self) ->str:
        return f"{self.center} represents the centerposition. The rectangles width is {self.width}, the hight is {self.height}"