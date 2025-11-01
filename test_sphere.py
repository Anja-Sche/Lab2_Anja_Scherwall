from pytest import raises
from sphere import Sphere

def test_valid_init():
    s = Sphere(1,1,3)
    assert s.x == 1 and s.y == 1 and s.radius == 3

def test_negative_placement_valid():
    s = Sphere(1,-2,3)
    assert s.x == 1 and s.y == -2 and s.radius == 3

def test_negative_radius_fail():
    with raises(ValueError):
        Sphere(1,2,-3)

def test_zero_radius_fail():
    with raises(ValueError):
        Sphere(1,1,0)

def test_string_init_fail():
    with raises(TypeError):
        Sphere(1,"2",3)
        Sphere(1,2,"3") 
        
def test_volume_valid():
    s = Sphere(1,1,3)
    assert s.volume == 113.0973
 
def test_circumference_valid():
    s = Sphere(1,1,3)
    assert s.circumference == 18.8496

def test_area_valid():
    s = Sphere(1,1,4)
    assert s.area == 201.0619

def test_dunder_repr():
    s = Sphere(1,1,4)
    assert repr(s) == "Sphere(x=1, y=1, radius=4)"

def test_dunder_str():
    s = Sphere(2,4,1)
    assert str(s) == "(2, 4) represents the centerposition. The spheres radius is 1"
