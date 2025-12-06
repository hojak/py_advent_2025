from day6.worksheet import Worksheet


def test_empty_worksheet():
    worksheet = Worksheet()

    assert worksheet.get_grand_total() == 0


def test_add_line():
    worksheet = Worksheet()
    worksheet.add_line("1 1 1 1")

    assert worksheet.get_grand_total() == 4
