from utils import same_shape
from utils import validate_different_type
from utils import validate_type_number

class Center:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        

    @property
    def x(self) -> None: 
        return self._x 
    
    @x.setter
    def x(self, value: int) -> int:
        validate_type_number(value)
        self._x = value

    @property
    def y(self) -> None: 
        return self._y 
    
    @y.setter
    def y(self, value: int) -> int:
        validate_type_number(value)
        self._y = value

        
    def translate(self, a: int, b: int) -> int:
        self._x = a
        self._y = b
        return self._x, self._y
    

    def __eq__(self, other) -> bool: 
        if same_shape(self, other):
            return True
        else:
            return False


    def __lt__(self, other) -> bool:
        validate_different_type(self, other)
                
        if self.area < other.area:
            return True
        else:
            return False


    def __le__(self, other) -> bool:
        validate_different_type(self, other) 
        
        if self.area <= other.area:
            return True
        else:
            return False      


    def __gt__(self, other) -> bool:
        validate_different_type(self, other) 
        
        if self.area > other.area:
            return True
        else:
            return False 


    def __ge__(self, other) -> bool:
        validate_different_type(self, other) 
        
        if self.area >= other.area:
            return True
        else:
            return False
