from center import Center

class Rectangle(Center):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        super().__init__(x, y)
        self.width = width
        self.height = height

        self._area = 0
        self._parimeter = 0

    @property
    def area(self) -> float:
        area = self.width*self.height
        self._area = area
        return self._area
    
    @property
    def perimeter(self) -> float:
        perimeter = (self.width*2)+(self.height*2)
        self._perimeter = perimeter
        return self._perimeter 
    
    def square(self) -> bool:
        if self.width == self.height:
            return True
        else:
            print("This is a rectangle, not a square")