class Bank:
    
    def __init__(self, bankstr: str):
        self.bankstr = bankstr

    def len(self) -> int:
        return len(self.bankstr)
    
    def battery(self, index: int) -> int:
        return int(self.bankstr[index])

    def highest_joltage(self) -> int:
        largest_first = 0
        index_of_first = 0

        for first_index in range(0, self.len()-1):
            int_at_first = self.battery(first_index)
            if (int_at_first > largest_first):
                largest_first = int_at_first
                index_of_first = first_index

        largest_second = 0
        for second_index in range(index_of_first+1, self.len()):
            int_at_second = self.battery(second_index)
            if (int_at_second > largest_second):
                largest_second = int_at_second

        return largest_first * 10 + largest_second

    def sum_of_joltages(banks: str) -> int:
        result = 0
        for bankstr in banks.splitlines():
            bank = Bank(bankstr)
            result += bank.highest_joltage()
        return result