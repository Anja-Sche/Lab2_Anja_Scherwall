from utils import same_shape

class Center:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        #create getter and setter?

        
    def translate(self, a: int, b: int) -> int:
        self.x = a
        self.y = b
        return self.x, self.y
    

    def __eq__(self, other) -> bool: 
        if same_shape(self, other) == True:
            return True
        else:
            return False


    def __lt__(self, other) -> bool:
        if same_shape(self, other) == True:    
            if self.area < other.area:
                return True
            else:
                return False
        else:
            print(f"They are not the same type") #raise error? Make a function?
            #få bort 'None' vid 'print()'?


    def __le__(self, other) -> bool:
        if same_shape(self, other) == True:    
            if self.area <= other.area:
                return True
            else:
                return False
        else:
            print(f"They are not the same type") #raise error? Make a function?        


    def __gt__(self, other) -> bool:
        if same_shape(self, other) == True:    
            if self.area > other.area:
                return True
            else:
                return False
        else:
            print(f"They are not the same type") #raise error? Make a function?


    def __ge__(self, other) -> bool:
        if same_shape(self, other) == True:    
            if self.area >= other.area:
                return True
            else:
                return False
        else:
            print(f"They are not the same type") #raise error? Make a function?
