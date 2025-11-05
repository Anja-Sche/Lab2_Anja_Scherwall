from center import Center
import utils

class Cube(Center):
    """
    A class representing the shape cube.

    Attributes:
    - x (int): The coordinate on the x axel.
    - y (int): The coordinate on the y axel.
    - z (int): The coordinate on the y axel.
    - side (int): The side of the cube.

    Operators:
    - operators for comparison: ==, <, <=, >, >= 

    Methods:
    - translate(): Moves the center position by adding to the existing one.

    Example usage:
    >>> cube1 = Cube(2, 1, 3)
    >>> cube1.translate(2, 1)
    >>> print(cube1)
    (4, 2) represents the centerposition. The cubes sides are 3.
    """

    def __init__(self, x:int|float=0, y:int|float=0, z:int|float=0, side: int|float=1) -> None:
        """
        Initializes an new instance of the class Cube.

        Parameters:
        - x (int): The coordinate on the x axel.
        - y (int): The coordinate on the y axel.
        - z (int): The coordinate on the y axel.
        - side (int): The side of the cube.
        """
        self.z = z
        super().__init__(x, y)
        self.side = side
        self.center = (self.x, self.y, self.z)

    @property
    def side(self) -> int|float:
        return self._side
    
    @side.setter
    def side(self, value: int|float) -> None:
        utils.validate_type_number(value)
        utils.validation_positive_number(value)

        self._side = value

    @property
    def z(self) -> int|float:         
        return self._z 
    
    @z.setter
    def z(self, value: int|float) -> None:
        utils.validate_type_number(value)
        self._z = value

    @property
    def center(self) -> tuple:        
        return self._center
    
    @center.setter
    def center(self, value) ->None:        
        self._center = (self._x, self._y, self._z)

    @property
    def volume(self) -> float:
        return round(self._side * self._side * self._side,4)
    
    @property
    def perimeter(self) -> float:
        return round(self._side * 12,4)
    
    @property 
    def area(self) -> float:
        return round((self._side * self._side) * 6,4)
    
    def translate(self, x: int|float, y: int|float, z: int|float) -> str:
        """Moves the center position by adding to the existing one."""
        self._x = self._x + x
        self._y = self._y + y
        self._z = self._z + z
        self._center = (self._x, self._y, self._z)
        return f"The new center of the shape is {self._center}"

    def __repr__(self) ->str:
        return f"Cube(x={self._x}, y={self._y}, z={self._z}, side={self._side})"
    
    def __str__(self) ->str:
        return f"{self._center} represents the centerposition. The cubes sides are {self._side}"