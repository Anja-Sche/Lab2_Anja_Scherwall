import utils  

class Center:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

        self.center = (self.x, self.y)

    
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

    @property
    def center(self):        
        return self._center
    
    @center.setter
    def center(self, value):        
        self._center = (self._x, self._y)

        
    def translate(self, x: int, y: int) -> int:
        self._x = self._x + x
        self._y = self._y + y
        self.center = (self._x, self._y)
        return self.center
        
    

    def __eq__(self, other) -> bool:         
        if utils.same_shape(self, other) and self.area == other.area and self.perimeter == other.perimeter:
            return True
        else:
            return False


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
