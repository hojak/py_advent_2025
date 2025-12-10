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

    pair = playground.get_closest_pair(0)
    assert pair == (JunctionBox(3, 3, 3), JunctionBox(4, 4, 4)) \
        or pair == (JunctionBox(4, 4, 4), JunctionBox(3, 3, 3))

    pair = playground.get_closest_pair(1)
    assert pair == (JunctionBox(3, 3, 3), JunctionBox(1, 1, 1)) \
        or pair == (JunctionBox(1, 1, 1), JunctionBox(3, 3, 3))

    pair = playground.get_closest_pair(2)
    assert pair == (JunctionBox(4, 4, 4), JunctionBox(1, 1, 1)) \
        or pair == (JunctionBox(1, 1, 1), JunctionBox(4, 4, 4))


def test_get_circuits_for_single_junction_box():
    playground = Playground()

    playground.add_junction_box(JunctionBox(1, 1, 1))

    circuits = list(playground.get_circuits())

    assert len(circuits) == 1
    assert circuits[0].get_size() == 1
    assert JunctionBox(1, 1, 1) in circuits[0].get_junction_boxes()


def test_get_initial_circuits_for_multiple_junction_boxes():
    playground = Playground()
    playground.add_junction_box(JunctionBox(1, 1, 1))
    playground.add_junction_box(JunctionBox(2, 2, 2))
    playground.add_junction_box(JunctionBox(3, 3, 3))

    circuits = list(playground.get_circuits())

    assert len(circuits) == 3
    assert sum(circuit.get_size() for circuit in circuits) == 3


def test_connect_two_boxes():
    playground = Playground()
    box_a = JunctionBox(1, 1, 1)
    box_b = JunctionBox(2, 2, 2)
    box_c = JunctionBox(3, 3, 3)
    playground.add_junction_box(box_a)
    playground.add_junction_box(box_b)
    playground.add_junction_box(box_c)

    playground.connect_boxes(box_a, box_b)

    circuits = list(playground.get_circuits())

    assert len(circuits) == 2
    assert box_a in circuits[0].get_junction_boxes() or \
        box_a in circuits[1].get_junction_boxes()
    assert box_b in circuits[0].get_junction_boxes() or \
        box_b in circuits[1].get_junction_boxes()
    assert box_c in circuits[0].get_junction_boxes() or \
        box_c in circuits[1].get_junction_boxes()

    assert sum(circuit.get_size() for circuit in circuits) == 3


def test_set_behaviour_of_playground():
    playground = Playground()

    playground.add_junction_box(JunctionBox(1, 1, 1))
    assert playground.get_number_of_circuits() == 1

    playground.add_junction_box(JunctionBox(2, 2, 2))
    assert playground.get_number_of_circuits() == 2

    playground.add_junction_box(JunctionBox(1, 1, 1))
    assert playground.get_number_of_circuits() == 2
