import utils  

class Center:
    """
    A class used to reprecent a shapes center position.

    Attributes:
    - x (int): The coordinate on the x axel.
    - y (int): The coordinate on the y axel.

    Dunder methods:
    - __eq__: Compare if two child-classes are equal. The same type, area and perimeter
    - __lt__: Check if a shape in child-class is smaller than another in same class. Compared by area.
    - __le__: Check if a shape in child-class is smaller or equal to another in same class. Compared by area.
    - __gt__: Check if a shape in child-class is greater than another in same class. Compared by area.
    - __ge__: Check if a shape in child-class is greater or equal to another in same class. Compared by area.

    Methods:
    - translate(): Moves the center position by adding to the existing one.
    
    Example usage:
    >>> center1 = Center(2, 3)
    >>> center1.translate(1, 3)
    >>> center1
    Center(x=3, y=6)
    """

    def __init__(self, x=0, y=0) -> None:
        """
        Initializes an new instance of the class Center.

        Parameters: 
        - x (int): The coordinate on the x axel.
        - y (int): The coordinate on the y axel.
        """
        self.x = x
        self.y = y

        self.center = (self.x, self.y)

    @property
    def x(self) -> int|float:         
        return self._x 
    
    @x.setter
    def x(self, value: int|float) -> None:
        utils.validate_type_number(value)
        self._x = value

    @property
    def y(self) -> int|float: 
        return self._y 
    
    @y.setter
    def y(self, value: int|float) -> None:
        utils.validate_type_number(value)        
        self._y = value

    @property
    def center(self) -> tuple:        
        return self._center
    
    @center.setter
    def center(self, value) ->None:        
        self._center = (self._x, self._y)    


    def __eq__(self, other) -> bool: 
        """Compare if two child-classes are equal. The same type, area and perimeter"""
        if utils.same_shape(self, other) and self.area == other.area and self.perimeter == other.perimeter:
            return True
        else:
            return False

    def __lt__(self, other) -> bool:
        """Check if a shape in child-class is smaller than another in same class. Compared by area."""
        utils.validate_different_type(self, other)
                
        if self.area < other.area:
            return True
        else:
            return False

    def __le__(self, other) -> bool:
        """Check if a shape in child-class is smaller or equal to another in same class. Compared by area."""
        utils.validate_different_type(self, other) 
        
        if self.area <= other.area:
            return True
        else:
            return False      

    def __gt__(self, other) -> bool:
        """Check if a shape in child-class is greater than another in same class. Compared by area."""
        utils.validate_different_type(self, other) 
        
        if self.area > other.area:
            return True
        else:
            return False

    def __ge__(self, other) -> bool:
        """Check if a shape in child-class is greater or equal to another in same class. Compared by area."""
        utils.validate_different_type(self, other) 
        
        if self.area >= other.area:
            return True
        else:
            return False
        

    def translate(self, x: int|float, y: int|float) -> str:
        """Puts x and y in a tuple."""
        self._x = self._x + x
        self._y = self._y + y
        self._center = (self._x, self._y)
        return f"The new center of the shape is {self._center}"

    def __repr__(self) ->str:
        return f"Center(x={self._x}, y={self._y})"
    
    def __str__(self) ->str:
        return f"{self.center} represents a centerposition of x and y."