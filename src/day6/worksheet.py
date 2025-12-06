class Worksheet:

    def __init__(self):
        self.number_sheet = []

    def get_grand_total(self) -> int:
        column_results = []

        for index in range(0, len(self.number_sheet)):
            column_results.append(self.column_result(index))

        return sum(column_results)

    def column_result(self, index: int) -> int:
        return sum(self.number_sheet[index])

    def add_line(self, line: str):
        numbers_in_line = line.split(' ')

        if (len(self.number_sheet) == 0):
            self.init_numbers(len(line))

        for index in range(0, len(numbers_in_line)):
            self.number_sheet[index].append(int(numbers_in_line[index]))

    def init_numbers(self, length):
        self.number_sheet = []
        for i in range(0, length):
            self.number_sheet.append([])