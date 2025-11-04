from center import Center
import utils

class Cube(Center):
    """
    A class representing the shape cube.

    Attributes:
    - x (int): The coordinate on the x axel.
    - y (int): The coordinate on the y axel.
    - side (int): The side of the cube.

    Methods:
    - translate(): Moves the center position by adding to the existing one.

    Example usage:
    >>> cube1 = Cube(2, 1, 3)
    >>> cube1.translate(2, 1)
    >>> print(cube1)
    (4, 2) represents the centerposition. The cubes sides are 3.
    """

    def __init__(self, x=0, y=0, side=0) -> None:
        """
        Initializes an new instance of the class Cube.

        Parameters:
        - x (int): The coordinate on the x axel.
        - y (int): The coordinate on the y axel.
        - side (int): The side of the cube.
        """
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
    def volume(self) -> float:
        return self._side * self._side * self._side
    
    @property
    def perimeter(self) -> float:
        return self._side * 12
    
    @property 
    def area(self) -> float:
        return (self._side * self._side) * 6
    
    def __repr__(self) ->str:
        return f"Cube(x={self._x}, y={self._y}, side={self._side})"
    
    def __str__(self) ->str:
        return f"{self._center} represents the centerposition. The cubes sides are {self._side}"