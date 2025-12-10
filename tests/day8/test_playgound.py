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


def test_check_value():
    playground = Playground()

    playground.add_junction_box(JunctionBox(1, 1, 1))
    playground.add_junction_box(JunctionBox(3, 3, 3))
    playground.add_junction_box(JunctionBox(4, 4, 4))
    playground.add_junction_box(JunctionBox(8, 8, 8))
    playground.add_junction_box(JunctionBox(9, 9, 9))

    playground.connect_boxes(JunctionBox(1, 1, 1), JunctionBox(3, 3, 3))
    playground.connect_boxes(JunctionBox(4, 4, 4), JunctionBox(8, 8, 8))

    assert playground.get_check_value() == 4


def test_excample():
    playground = Playground.create_from_string(
'''162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
''')
    
    for i in range(0, 10):
        pair = playground.get_closest_pair(i)
        playground.connect_boxes(pair[0], pair[1])

    assert playground.get_check_value() == 40
