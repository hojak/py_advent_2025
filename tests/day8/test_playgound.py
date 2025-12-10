from day8.junctionBox import JunctionBox
from day8.playground import Playground


def test_create_with_three_junction_boxes():
    playground = Playground()

    playground.add_junction_box(JunctionBox(1, 1, 1))
    playground.add_junction_box(JunctionBox(2, 2, 2))
    playground.add_junction_box(JunctionBox(3, 3, 3))

    assert playground.number_of_boxes() == 3


def test_get_closest_pairs():
    playground = Playground()

    playground.add_junction_box(JunctionBox(1, 1, 1))
    playground.add_junction_box(JunctionBox(3, 3, 3))
    playground.add_junction_box(JunctionBox(4, 4, 4))
    playground.add_junction_box(JunctionBox(8, 8, 8))

    assert (JunctionBox(3, 3, 3), JunctionBox(4, 4, 4)) == \
        playground.get_closest_pair(0)
    assert (JunctionBox(1, 1, 1), JunctionBox(3, 3, 3)) == \
        playground.get_closest_pair(1)
    assert (JunctionBox(1, 1, 1), JunctionBox(4, 4, 4)) == \
        playground.get_closest_pair(2)


def test_get_circuits_for_single_junction_box():
    playground = Playground()

    playground.add_junction_box(JunctionBox(1, 1, 1))

    circuits = playground.get_circuits()

    assert len(circuits) == 1
    assert circuits[0].get_size() == 1
    assert circuits[0].get_junction_boxes() == [JunctionBox(1, 1, 1)]


def test_get_initial_circuits_for_multiple_junction_boxes():
    playground = Playground()
    playground.add_junction_box(JunctionBox(1, 1, 1))
    playground.add_junction_box(JunctionBox(2, 2, 2))
    playground.add_junction_box(JunctionBox(3, 3, 3))

    circuits = playground.get_circuits()

    assert len(circuits) == 3
    assert sum(circuit.get_size() for circuit in circuits) == 3
