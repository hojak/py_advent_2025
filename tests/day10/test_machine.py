from day10.machine import Machine


def test_init_from_string():
    machine = Machine("[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}")

    assert machine is not None
    assert machine.get_indicator_lights().number_of_lights() == 4
    assert len(machine.get_buttons()) == 6


def test_number_of_lights():
    machine = Machine("[.##.#.] (3) (1,3) (2) (2,3) (0,1) {3,5,4,7}")

    assert machine.get_indicator_lights().number_of_lights() == 6


def test_button_initialization():
    machine = Machine("[.##.#.] (3) (1,3) (2) (2,3) (0,1) {3,5,4,7}")

    assert len(machine.get_buttons()) == 5
    assert machine.get_buttons()[0].connected_lights == [3]
    assert machine.get_buttons()[1].connected_lights == [1, 3]


def test_get_target_light_configuration():
    machine = Machine("[.##.#.] (3) (1,3) (2) (2,3) (0,1) {3,5,4,7}")

    assert machine.target_light_configuration == '.##.#.'


def test_get_minimal_buttons_to_press():
    machine = Machine("[...#] (0) (0,1) (1,2) (2,3) {1,2,3}")

    assert len(machine.get_minimal_buttons_sequence()) == 4


def test_create_lightning_configurations():
    assert Machine.create_all_light_configurations(3) == [
        '...', '..#', '.#.', '.##', '#..', '#.#', '##.', '###'
    ]
