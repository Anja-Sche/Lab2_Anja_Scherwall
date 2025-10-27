from center import Center

class Circle(Center):
    def __init__(self, x= 0, y= 0, radius = 0) -> None: #place radius first for no default value??
        super().__init__(x, y)
        self.radius = radius

        self._area = 0
        self._parimeter = 0

    @property
    def area(self) -> float:
        area = (self.radius*self.radius)*3.14
        self._area = area
        return self._area
    #fix float?
    
    @property
    def perimeter(self) -> float:
        perimeter = (self.radius + self.radius)*3.14
        self._perimeter = perimeter
        return self._perimeter 
    #fix float?

    def unit_circle(self) -> bool:
        if self.x == 0 and self.y == 0 and self.radius == 1:
            return True
        else:
            return False