def same_shape(self, other):
    if type(self) == type(other):
        return True
    else:
        return False
    

def validate_different_type(self, other):
    if not (same_shape(self, other)):    
        raise TypeError("You can't compare size of two different shapes.")
    

def validate_type_number(value):
    if not isinstance(value, int):
        raise TypeError(f"Value must contain digits, not {type(value)}")
    

def validation_positive_number(value):
    if not 0 < value:
        raise ValueError(f"Value must be lager than 0")