from pytest import raises
from sphere import Sphere
from cube import Cube

def test_valid_init():
    s = Sphere(1,1,2,3)
    assert s.x == 1 and s.y == 1 and s.z == 2 and s.radius == 3

def test_negative_placement_valid():
    s = Sphere(1,-2,2,3)
    assert s.x == 1 and s.y == -2 and s.z == 2 and s.radius == 3

def test_negative_radius_fail():
    with raises(ValueError):
        Sphere(1,2,1,-3)

def test_zero_radius_fail():
    with raises(ValueError):
        Sphere(1,1,1,0)

def test_string_init_fail():
    with raises(TypeError):
        Sphere(1,"2",2,3)
        Sphere(1,2,1,"3") 
        
def test_volume_valid():
    s = Sphere(1,1,2,3)
    assert s.volume == 113.0973
 
def test_circumference_valid():
    s = Sphere(1,1,2,3)
    assert s.circumference == 18.8496

def test_area_valid():
    s = Sphere(1,1,2,4)
    assert s.area == 201.0619

def test_translate_valid():
    s = Sphere(1,2,3,4)
    s.translate(1,2,3)
    assert s.x == 2 and s.y == 4 and s.z == 6 and s.radius == 4

def test_equal_valid():
    s1 = Sphere(1,1,2,4)
    s2 = Sphere(2,1,3,4)
    assert (s1==s2) == True

def test_not_equal():
    s1 = Sphere(1,1,2,4)
    s2 = Sphere(2,1,3,2)
    assert (s1==s2) == False

def test_not_equal_different_shape():
    s = Sphere(1,1,2,4)
    c = Cube(1,1,2,4)
    with raises(TypeError):
        (s==c)

def test_larger_than_valid():
    s1 = Sphere(1,1,2,4)
    s2 = Sphere(2,1,3,2)
    assert (s1>s2) == True

def test_larger_than_false():
    s1 = Sphere(1,1,2,4)
    s2 = Sphere(2,1,3,2)
    assert (s2>s1) == False

def test_larger_than_equal_valid():
    s1 = Sphere(1,1,2,4)
    s2 = Sphere(2,1,3,2)
    s3 = Sphere(3,1,4,2)
    assert (s1>=s2) == True and (s1>=s3) == True

def test_larger_than_equal_false():
    s1 = Sphere(1,1,2,4)
    s2 = Sphere(2,1,3,2)
    assert (s2>=s1) == False

def test_lesser_than_valid():
    s1 = Sphere(1,1,2,2)
    s2 = Sphere(2,1,3,4)
    assert (s1<s2) == True    

def test_lesser_than_false():
    s1 = Sphere(1,1,2,2)
    s2 = Sphere(2,1,3,4)
    assert (s2<s1) == False

def test_lesser_than_equal_valid():
    s1 = Sphere(1,1,1,3)
    s2 = Sphere(2,1,2,4)
    s3 = Sphere(3,1,3,3)
    assert (s1<=s2) == True and (s1<=s3) == True

def test_lesser_than_equal_false():
    s1 = Sphere(1,1,2,2)
    s2 = Sphere(2,1,3,4)
    assert (s2<=s1) == False

def test_dunder_repr():
    s = Sphere(1,1,1,4)
    assert repr(s) == "Sphere(x=1, y=1, z=1, radius=4)"

def test_dunder_str():
    s = Sphere(2,4,2,1)
    assert str(s) == "(2, 4, 2) represents the centerposition. The spheres radius is 1"
