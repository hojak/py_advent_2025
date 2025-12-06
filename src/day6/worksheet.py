class Worksheet:

    def __init__(self):
        self.number_sheet = []
        self.operants = []

    def get_grand_total(self) -> int:
        column_results = []

        for index in range(0, len(self.number_sheet)):
            column_results.append(self.column_result(index))

        return sum(column_results)

    def column_result(self, index: int) -> int:
        if (len(self.operants) >= index+1):
            operant = self.operants[index]
        else:
            operant = "+"

        if (operant == "*"):
            return self.multiply_column(index)
        else:
            return self.add_column(index)

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

    def set_operants(self, operants_string: str):
        self.operants = operants_string.split(' ')

    def add_column(self, index):
        return sum(self.number_sheet[index])

    def multiply_column(self, index):
        result = 1
        for factor in self.number_sheet[index]:
            result *= factor
        return result
