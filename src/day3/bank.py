class Bank:
    
    def __init__(self, bankstr: str):
        self.bankstr = "0"+bankstr

    def len(self) -> int:
        return len(self.bankstr)
    
    def battery(self, index: int) -> int:
        return int(self.bankstr[index])

    def highest_joltage(self, size=2) -> int:
        indices = list(range(self.len()-size+1, self.len()+1))
        indices.insert(0, 0)

        for digit in range(1, size+1):
            largest_found = 0
            for index in range(indices[digit-1]+1, indices[digit]):
                found_int = self.battery(index)
                if (found_int > largest_found):
                    largest_found = found_int
                    indices[digit] = index

        return self.get_power(indices)

    def get_power(self, indices: list[int]) -> int:
        str = ""
        for index in indices:
            str += self.bankstr[index]

        return int(str)

    def sum_of_joltages(banks: str, size=2) -> int:
        result = 0
        for bankstr in banks.splitlines():
            bank = Bank(bankstr)
            result += bank.highest_joltage(size)
        return result
