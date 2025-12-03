def highest_joltage(bank: str) -> int:
    largest_first = 0
    index_of_first = 0

    for first_index in range(0, len(bank)-1):
        int_at_first = int(bank[first_index])
        if (int_at_first > largest_first):
            largest_first = int_at_first
            index_of_first = first_index

    largest_second = 0
    for second_index in range(index_of_first+1, len(bank)):
        int_at_second = int(bank[second_index])
        if (int_at_second > largest_second):
            largest_second = int_at_second

    return largest_first * 10 + largest_second


def sum_of_joltages(banks: str) -> int:
    result = 0
    for bank in banks.splitlines():
        result += highest_joltage(bank)
    return result