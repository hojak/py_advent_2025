from day8.circuit import Circuit
from day8.junctionBox import JunctionBox


def test_set_behaviour_of_circuits():
    circuit = Circuit()

    circuit.add_junction_box(JunctionBox(1, 1, 1))
    assert circuit.get_size() == 1

    circuit.add_junction_box(JunctionBox(2, 2, 2))
    assert circuit.get_size() == 2

    circuit.add_junction_box(JunctionBox(1, 1, 1))
    assert circuit.get_size() == 2
