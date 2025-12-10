from math import sqrt
from day8.junctionBox import JunctionBox


def test_create():
    box = JunctionBox(1, 2, 3)
    assert box.x == 1
    assert box.y == 2
    assert box.z == 3


def test_distance():
    box_a = JunctionBox(0, 0, 0)
    box_b = JunctionBox(10, 10, 10)
    
    assert box_a.distance_to(box_b) == box_b.distance_to(box_a) == sqrt(300)
