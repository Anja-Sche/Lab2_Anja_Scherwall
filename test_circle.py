from pytest import raises
from circle import Circle

def test_valid_init():
    c = Circle(x=1, y=1, radius=3)
    assert c.x == 1 and c.y == 1 and c.radius == 3

def test_negative_placement():
    c = Circle(1,-2,3)
    assert c.x == 1 and c.y == -2 and c.radius == 3

def test_negative_radius_fail():
    with raises(ValueError):
        Circle(1,2,-3)

def test_string_init_fail():
    with raises(TypeError):
        Circle(1,"2",3)
        Circle(1,2,"3")