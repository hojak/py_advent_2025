class Bank:
    
    def __init__(self, bankstr: str):
        self.bankstr = "0"+bankstr

    def len(self) -> int:
        return len(self.bankstr)
    
    def battery(self, index: int) -> int:
        return int(self.bankstr[index])

    def highest_joltage(self, size=2) -> int:
        indices = [0, self.len()-1, self.len()]

        largest_found = 0
        for index in range(indices[0], indices[1]):
            found_int = self.battery(index)
            if (found_int > largest_found):
                largest_found = found_int
                indices[1] = index

        largest_found = 0
        for index in range(indices[1]+1, indices[2]):
            found_int = self.battery(index)
            if (found_int > largest_found):
                largest_found = found_int
                indices[2] = index

        return self.get_power(indices)
    
    def get_power(self, indices: list[int]) -> int:
        str = ""
        for index in indices:
            str += self.bankstr[index]
        return int(str)

    def sum_of_joltages(banks: str) -> int:
        result = 0
        for bankstr in banks.splitlines():
            bank = Bank(bankstr)
            result += bank.highest_joltage()
        return result