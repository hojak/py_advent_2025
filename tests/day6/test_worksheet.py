from day6.worksheet import Worksheet


def test_empty_worksheet():
    worksheet = Worksheet()

    assert worksheet.get_grand_total() == 0
