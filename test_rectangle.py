from pytest import raises
from rectangle import Rectangle
from sphere import Sphere
from cube import Cube


def test_valid_init():
    r = Rectangle(x=1, y=1, width=3, height=2)
    assert r.x == 1 and r.y == 1 and r.width == 3 and r.height == 2

def test_negative_placement_valid():
    r = Rectangle(1,-2,3,4)
    assert r.x == 1 and r.y == -2 and r.width == 3 and r.height == 4

def test_negative_radius_fail():
    with raises(ValueError):
        Rectangle(1,2,-3,2)

def test_zero_radius_fail():
    with raises(ValueError):
        Rectangle(1,1,0,2)

def test_string_init_fail():
    with raises(TypeError):
        Rectangle(1,"2",3,4)
        Rectangle(1,2,"3",2)

def test_perimeter_valid():
    r = Rectangle(1,1,3,2)
    assert r.perimeter == 10

def test_area_valid():
    r = Rectangle(1,1,4,2)
    assert r.area == 8

def test_translate_valid():
    r = Rectangle(1,2,3,4)
    r.translate(1,2)
    assert r.x == 2 and r.y == 4 and r.width == 3 and r.height == 4

def test_equal_valid():
    r1 = Rectangle(1,1,4,2)
    r2 = Rectangle(2,1,2,4)
    assert (r1==r2) == True

def test_not_equal():
    r1 = Rectangle(1,1,4,3)
    r2 = Rectangle(2,1,2,3)
    assert (r1==r2) == False

def test_not_equal_different_shape():
    r = Rectangle(1,1,2,4)
    s = Sphere(1,1,2,4)
    assert (r==s) == False

def test_larger_than_valid():
    r1 = Rectangle(1,1,4,3)
    r2 = Rectangle(2,1,3,2)
    assert (r1>r2) == True

def test_larger_than_false():
    r1 = Rectangle(1,1,4,3)
    r2 = Rectangle(2,1,2,3)
    assert (r2>r1) == False

def test_larger_than_equal_valid():
    r1 = Rectangle(1,1,4,2)
    r2 = Rectangle(2,1,2,3)
    r3 = Rectangle(3,1,3,2)
    assert (r1>=r2) == True and (r1>=r3) == True

def test_larger_than_equal_false():
    r1 = Rectangle(1,1,4,2)
    r2 = Rectangle(2,1,3,2)
    assert (r2>=r1) == False and (r2==r1) == False

def test_lesser_than_valid():
    r1 = Rectangle(1,1,3,2)
    r2 = Rectangle(2,1,4,3)
    assert (r1<r2) == True    

def test_lesser_than_false():
    r1 = Rectangle(1,1,3,2)
    r2 = Rectangle(2,1,4,2)
    assert (r2<r1) == False and (r2==r1) == False

def test_lesser_than_equal_valid():
    r1 = Rectangle(1,1,3,2)
    r2 = Rectangle(2,1,4,2)
    r3 = Rectangle(3,1,2,3)
    assert (r1<=r2) == True and (r1==r3) == True

def test_lesser_than_equal_false():
    r1 = Rectangle(1,1,3,1)
    r2 = Rectangle(2,1,4,2)
    assert (r2<=r1) == False

def test_dunder_repr():
    r = Rectangle(1,1,4,2)
    assert repr(r) == "Rectangle(x=1, y=1, width=4, height=2)"

def test_dunder_str():
    r = Rectangle(2,4,1,2)
    assert str(r) == "(2, 4) represents the centerposition. The rectangles width is 1, the hight is 2"
