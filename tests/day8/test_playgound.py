from day8.junctionBox import JunctionBox
from day8.playground import Playground


def test_create_with_three_junction_boxes():
    playground = Playground()

    playground.add_junction_box(JunctionBox(1, 1, 1))
    playground.add_junction_box(JunctionBox(2, 2, 2))
    playground.add_junction_box(JunctionBox(3, 3, 3))

    assert playground.number_of_boxes() == 3
