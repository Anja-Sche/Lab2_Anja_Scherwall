import utils  

class Center:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        

    def __repr__(self):
        return f"Center(x={self.x}, y={self.y})"
    
    def __str__(self):
        return f"({self.x},{self.y}) represents the centerposition"


    @property
    def x(self) -> None: 
        return self._x 
    
    @x.setter
    def x(self, value: int) -> int:
        utils.validate_type_number(value)
        self._x = value

    @property
    def y(self) -> None: 
        return self._y 
    
    @y.setter
    def y(self, value: int) -> int:
        utils.validate_type_number(value)
        self._y = value

        
    def translate(self, x: int, y: int) -> int:
        self._x = self._x + x
        self._y = self._y + y
        return self._x, self._y
        #???????
    

    def __eq__(self, other) -> bool: 
        if utils.same_shape(self, other):
            if not self.area == other.area and self.perimeter == other.perimeter:
                return False
        else:
            return True


    def __lt__(self, other) -> bool:
        utils.validate_different_type(self, other)
                
        if self.area < other.area:
            return True
        else:
            return False


    def __le__(self, other) -> bool:
        utils.validate_different_type(self, other) 
        
        if self.area <= other.area:
            return True
        else:
            return False      


    def __gt__(self, other) -> bool:
        utils.validate_different_type(self, other) 
        
        if self.area > other.area:
            return True
        else:
            return False 


    def __ge__(self, other) -> bool:
        utils.validate_different_type(self, other) 
        
        if self.area >= other.area:
            return True
        else:
            return False
