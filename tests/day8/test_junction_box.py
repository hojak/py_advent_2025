from day8.junctionBox import JunctionBox


def test_create():
    box = JunctionBox(1, 2, 3)
    assert box.x == 1
    assert box.y == 2
    assert box.z == 3
    