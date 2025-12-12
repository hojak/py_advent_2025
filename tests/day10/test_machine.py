from day10.machine import Machine


def test_init_from_string():
    machine = Machine("[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}")

    assert machine is not None
    assert machine.get_indicator_lights().number_of_lights() == 4
    assert len(machine.get_buttons()) == 6


def test_number_of_lights():
    machine = Machine("[.##.#.] (3) (1,3) (2) (2,3) (0,1) {3,5,4,7}")

    assert machine.get_indicator_lights().number_of_lights() == 6
