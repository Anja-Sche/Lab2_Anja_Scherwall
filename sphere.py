from circle import Circle
import utils
import numpy as np

class Sphere(Circle):
    """
    A class representing the shape sphere.

    Attributes:
    - x (int): The coordinate on the x axel.
    - y (int): The coordinate on the y axel.
    - z (int): The coordinate on the y axel.
    - radius (int): The radius of the sphere.

    Operators:
    - operators for comparison: ==, <, <=, >, >= 

    Methods:
    - translate(): Moves the center position by adding to the existing one.

    Example usage:
    >>> sphere1 = Sphere(1, 2, 2)
    >>> sphere1.translate(2, 2)
    >>> sphere1
    Sphere(x=3, y=4, radius=2)
    >>> sphere1.circumference
    12.5664
    """

    def __init__(self, x:int|float= 0, y:int|float= 0, z:int|float= 0, radius: int|float=1) -> None:
        """
        Initializes an new instance of the class Sphere.

        Parameters:
        - x (int): The coordinate on the x axel.
        - y (int): The coordinate on the y axel.
        - z (int): The coordinate on the y axel.
        - radius (int): The radius of the sphere.
        """
        self.z = z
        super().__init__(x, y, radius)
        self.center = (self.x, self.y, self.z)

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
        return round(((self.radius**3)*np.pi*4)/3, 4)
    
    @property
    def circumference(self) -> float:
        return round(self.perimeter, 4)
        
    @property
    def area(self) -> float:
        return round((self.radius*self.radius)*np.pi*4, 4)
    
    def translate(self, x: int|float, y: int|float, z: int|float) -> str:
        """Moves the center position by adding to the existing one."""
        self._x = self._x + x
        self._y = self._y + y
        self._z = self._z +z
        self._center = (self._x, self._y, self._z)
        return f"The new center of the shape is {self._center}"
    
    def __repr__(self) ->str:
        return f"Sphere(x={self._x}, y={self._y}, z={self._z}, radius={self.radius})"
    
    def __str__(self) ->str:
        return f"{self._center} represents the centerposition. The spheres radius is {self.radius}"