from numbers import Number

def validate_different_type(self, other):
    if not (type(self) == type(other)):    
        raise TypeError("You can't compare size of two different shapes.")
    

def validate_type_number(value):
    if isinstance(value, bool):
        raise TypeError(f"Value must be a number, not {type(value)}")
    if not isinstance(value, Number):
        raise TypeError(f"Value must be a number, not {repr(type(value))}")
    

def validation_positive_number(value):
    if not 0 < value:
        raise ValueError(f"Value must be lager than 0")