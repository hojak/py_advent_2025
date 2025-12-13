from day10.button import Button
from day10.joltageStatus import JoltageStatus


def test_joltage_status():
    status = JoltageStatus([1, 0, 0, 2])
    assert status.status == [1, 0, 0, 2]


def test_press_button():
    status = JoltageStatus([3, 2, 1, 0])
    new_status = status.push_button(Button("0,1"))
    assert new_status.status == [4, 3, 1, 0]


def test_joltage_to_high_for():
    status = JoltageStatus([5, 4, 3, 2])

    assert status.joltage_to_high_for([3, 4, 5, 6]) is True
    assert status.joltage_to_high_for([10, 10, 50, 60]) is False
