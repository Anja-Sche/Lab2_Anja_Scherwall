from center import Center
import numpy as np
import utils

class Circle(Center):
    """
    A class representing the shape circle.

    Attributes:
    - x (int): The coordinate on the x axel.
    - y (int): The coordinate on the y axel.
    - radius (int): The radius of the circle.

    Methods:
    - translate(): Moves the center position by adding to the existing one.
    - unit_circle(): Checks if the circle is a unit circle.

    Example usage:
    >>> circle1 = Circle(0, 0, 1)
    >>> circle1.unit_circle()
    True
    >>> circle1.translate(3, 4)
    >>> circle1
    Circle(x=3, y=4, radius=1)
    """

    def __init__(self, radius: int|float, x= 0, y= 0) -> None:
        """
        Initializes an new instance of the class Circle.

        Parameters:
        - x (int): The coordinate on the x axel.
        - y (int): The coordinate on the y axel.
        - radius (int): The radius of the circle.
        """
        super().__init__(x, y)
        self.radius = radius

    @property
    def radius(self) -> int|float:
        return self._radius
    
    @radius.setter
    def radius(self, value: int|float) -> None:
        utils.validate_type_number(value)
        utils.validation_positive_number(value)

        self._radius = value
    
    @property
    def area(self) -> float:
        return round((self.radius*self.radius)*np.pi,4)
    
    @property
    def perimeter(self) -> float:
        return round((self.radius*np.pi)*2,4)

    def unit_circle(self) -> bool:
        """Checks if the circle is a unit circle"""
        if self.center == (0, 0) and self._radius == 1:
            return True
        else:
            return False
        
    def __repr__(self) ->str:
        return f"Circle(x={self._x}, y={self._y}, radius={self.radius})"
    
    def __str__(self) ->str:
        return f"{self.center} represents the centerposition. The circles radius is {self.radius}"
        

    
