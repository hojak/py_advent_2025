from day6.worksheet import Worksheet


def test_empty_worksheet():
    worksheet = Worksheet()

    assert worksheet.get_grand_total() == 0


def test_add_line():
    worksheet = Worksheet()
    worksheet.add_line("1 1 1 1")

    assert worksheet.get_grand_total() == 4


def test_add_lines():
    worksheet = Worksheet()
    worksheet.add_line("1 1 1 1")
    worksheet.add_line("2 2 2 2")

    assert worksheet.get_grand_total() == 12
    
    
def test_set_operants():   
    worksheet = Worksheet()
    worksheet.add_line("1 1 1 1")
    worksheet.add_line("2 3 2 4")
    
    worksheet.set_operants("+ * + *")

    assert worksheet.get_grand_total() == 13
    
    
def test_multiply_white_spaces():
    worksheet = Worksheet()
    worksheet.add_line("1  1  1    1  ")
    
    assert worksheet.get_grand_total() == 4    
