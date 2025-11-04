from circle import Circle
import numpy as np

class Sphere(Circle):
    """
    A class representing the shape sphere.

    Attributes:
    - x (int): The coordinate on the x axel.
    - y (int): The coordinate on the y axel.
    - radius (int): The radius of the sphere.

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

    def __init__(self, x: 0, y: 0, radius: 0) -> None:
        """
        Initializes an new instance of the class Sphere.

        Parameters:
        - x (int): The coordinate on the x axel.
        - y (int): The coordinate on the y axel.
        - radius (int): The radius of the sphere.
        """
        super().__init__(x, y, radius)

    @property    
    def volume(self) -> float:
        return round(((self.radius**3)*np.pi*4)/3, 4)
    
    @property
    def circumference(self) -> float:
        return round(self.perimeter, 4)
        
    @property
    def area(self) -> float:
        return round((self.radius*self.radius)*np.pi*4, 4)
    
    def __repr__(self) ->str:
        return f"Sphere(x={self.x}, y={self.y}, radius={self.radius})"
    
    def __str__(self) ->str:
        return f"{self._center} represents the centerposition. The spheres radius is {self.radius}"