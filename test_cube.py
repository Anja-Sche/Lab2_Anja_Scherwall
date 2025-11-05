from pytest import raises
from cube import Cube

def test_valid_init():
    c = Cube(1,1,2,5)
    assert c.x == 1 and c.y == 1 and c.z == 2 and c.side == 5

def test_negative_placement_valid():
    c = Cube(1,-2,2,3)
    assert c.x == 1 and c.y == -2 and c.z == 2 and c.side == 3 

def test_negative_side_fail():
    with raises(ValueError):
        Cube(1,2,2,-3)

def test_zero_side_fail():
    with raises(ValueError):
        Cube(1,1,2,0)

def test_string_init_fail():
    with raises(TypeError):
        Cube(1,"2",2,3)
        Cube(1,2,2,"3") 
        
def test_volume_valid():
    c = Cube(1,1,2,3)
    assert c.volume == 27
 
def test_circumference_valid():
    c = Cube(1,1,2,3)
    assert c.perimeter == 36

def test_area_valid():
    c = Cube(1,1,2,4)
    assert c.area == 96

def test_dunder_repr():
    c = Cube(1,1,2,4)
    assert repr(c) == "Cube(x=1, y=1, z=2, side=4)"

def test_dunder_str():
    c = Cube(3,4,2,1)
    assert str(c) == "(3, 4, 2) represents the centerposition. The cubes sides are 1"
    # help from LLM how to test __repr__ and __str__