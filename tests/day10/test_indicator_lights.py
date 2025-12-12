from day10.button import Button
from day10.indicatorLights import IndicatorLights


def test_push_a_button_turns_on_lights():
    lights = IndicatorLights("..#")
    pushed_lights = lights.push_button(Button("0,1"))

    assert pushed_lights.__str__() == "###"


def test_push_a_button_turns_off_lights():
    lights = IndicatorLights("..##")
    pushed_lights = lights.push_button(Button("2,3"))

    assert pushed_lights.__str__() == "...."


def test_push_a_button_turns_toggles_lights():
    lights = IndicatorLights("..##")
    pushed_lights = lights.push_button(Button("1,2"))

    assert pushed_lights.__str__() == ".#.#"
