from pytest import raises
from cube import Cube
from sphere import Sphere

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

def test_translate_valid():
    c = Cube(1,2,3,4)
    c.translate(1,2,3)
    assert c.x == 2 and c.y == 4 and c.z == 6 and c.side == 4

def test_equal_valid():
    c1 = Cube(1,1,2,3)
    c2 = Cube(2,1,3,3)
    assert (c1==c2) == True

def test_not_equal():
    c1 = Cube(1,1,2,4)
    c2 = Cube(2,1,3,2)
    assert (c1==c2) == False

def test_not_equal_different_shape():
    s = Sphere(1,1,2,4)
    c = Cube(1,1,2,4)
    with raises(TypeError):
        (s==c)

def test_larger_than_valid():
    c1 = Cube(1,1,2,4)
    c2 = Cube(2,1,3,2)
    assert (c1>c2) == True

def test_larger_than_false():
    c1 = Cube(1,1,2,4)
    c2 = Cube(2,1,3,2)
    assert (c2>c1) == False

def test_larger_than_equal_valid():
    c1 = Cube(1,1,2,4)
    c2 = Cube(2,1,3,2)
    c3 = Cube(3,1,4,2)
    assert (c1>=c2) == True and (c1>=c3) == True

def test_larger_than_equal_false():
    c1 = Cube(1,1,2,4)
    c2 = Cube(2,1,3,2)
    assert (c2>=c1) == False

def test_lesser_than_valid():
    c1 = Cube(1,1,2,2)
    c2 = Cube(2,1,3,4)
    assert (c1<c2) == True    

def test_lesser_than_false():
    c1 = Cube(1,1,2,2)
    c2 = Cube(2,1,3,4)
    assert (c2<c1) == False

def test_lesser_than_equal_valid():
    c1 = Cube(1,1,1,3)
    c2 = Cube(2,1,2,4)
    c3 = Cube(3,1,3,3)
    assert (c1<=c2) == True and (c1<=c3) == True

def test_lesser_than_equal_false():
    c1 = Cube(1,1,2,2)
    c2 = Cube(2,1,3,4)
    assert (c2<=c1) == False

def test_dunder_repr():
    c = Cube(1,1,2,4)
    assert repr(c) == "Cube(x=1, y=1, z=2, side=4)"

def test_dunder_str():
    c = Cube(3,4,2,1)
    assert str(c) == "(3, 4, 2) represents the centerposition. The cubes sides are 1"
    # help from LLM how to test __repr__ and __str__