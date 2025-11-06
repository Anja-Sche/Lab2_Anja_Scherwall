from pytest import raises
from circle import Circle
from sphere import Sphere

def test_valid_init():
    c = Circle(x=1, y=1, radius=3)
    assert c.x == 1 and c.y == 1 and c.radius == 3

def test_negative_placement_valid():
    c = Circle(1,-2,3)
    assert c.x == 1 and c.y == -2 and c.radius == 3

def test_negative_radius_fail():
    with raises(ValueError):
        Circle(1,2,-3)

def test_zero_radius_fail():
    with raises(ValueError):
        Circle(1,1,0)

def test_string_init_fail():
    with raises(TypeError):
        Circle(1,"2",3)
        Circle(1,2,"3")

def test_perimeter_valid():
    c = Circle(1,1,3)
    assert c.perimeter == 18.8496

def test_area_valid():
    c = Circle(1,1,4)
    assert c.area == 50.2655

def test_translate_valid():
    c = Circle(1,2,3)
    c.translate(1,2)
    assert c.x == 2 and c.y == 4 and c.radius == 3

def test_unit_circle_valid():
    c = Circle(0,0,1)
    assert c.unit_circle() == True

def test_unit_circle_false():
    c = Circle(1,1,1)
    assert c.unit_circle() == False

def test_equal_valid():
    c1 = Circle(1,1,4)
    c2 = Circle(2,1,4)
    assert (c1==c2) == True

def test_not_equal():
    c1 = Circle(1,1,4)
    c2 = Circle(2,1,2)
    assert (c1==c2) == False

def test_not_equal_different_shape():
    c = Circle(1,1,4)
    s = Sphere(1,1,2,4)
    with raises(TypeError):
        c==s

def test_larger_than_valid():
    c1 = Circle(1,1,4)
    c2 = Circle(2,1,3)
    assert (c1>c2) == True

def test_larger_than_false():
    c1 = Circle(1,1,4)
    c2 = Circle(2,1,2)
    assert (c2>c1) == False

def test_larger_than_equal_valid():
    c1 = Circle(1,1,4)
    c2 = Circle(2,1,2)
    c3 = Circle(3,1,2)
    assert (c1>=c2) == True and (c1>=c3) == True

def test_larger_than_equal_false():
    c1 = Circle(1,1,4)
    c2 = Circle(2,1,2)
    assert (c2>=c1) == False and (c2==c1) == False

def test_lesser_than_valid():
    c1 = Circle(1,1,3)
    c2 = Circle(2,1,4)
    assert (c1<c2) == True    

def test_lesser_than_false():
    c1 = Circle(1,1,3)
    c2 = Circle(2,1,4)
    assert (c2<c1) == False and (c2==c1) == False

def test_lesser_than_equal_valid():
    c1 = Circle(1,1,3)
    c2 = Circle(2,1,4)
    c3 = Circle(3,1,3)
    assert (c1<=c2) == True and (c1==c3) == True

def test_lesser_than_equal_false():
    c1 = Circle(1,1,3)
    c2 = Circle(2,1,4)
    assert (c2<=c1) == False

def test_dunder_repr():
    c= Circle(1,1,4)
    assert repr(c) == "Circle(x=1, y=1, radius=4)"

def test_dunder_str():
    c= Circle(2,4,1)
    assert str(c) == "(2, 4) represents the centerposition. The circles radius is 1"
