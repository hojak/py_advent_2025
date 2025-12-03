from math import floor


class IdValidator:

    possible_number_of_parts = []

    def __init__(self, possible_number_of_parts=[2]) -> None:
        self.possible_number_of_parts = possible_number_of_parts

    def is_valid(self, some_id) -> bool:
        if (isinstance(some_id, int)):
            some_id = str(some_id)

        for number_of_parts in self.possible_number_of_parts:
            if self.is_repeated_pattern(some_id, number_of_parts):
                return False
            
        return True
    
    def is_repeated_pattern(self, some_id: str, number_of_parts: int) -> bool:
        if len(some_id) % number_of_parts != 0:
            return False
        
        part_length = floor(len(some_id) / number_of_parts)
        possible_part = some_id[:part_length]
        return some_id == possible_part * number_of_parts

    def get_invalid_ids(self, start: int, end: int) -> list:
        result = []
        for id in range(start, end+1):
            if (not self.is_valid(id)):
                result.append(id)
        return result

    def get_checksum(self, input: str) -> int:
        result = 0
        ranges = input.split(",")
        for range in ranges:
            (start, end) = range.split("-")
            invalid_ids = self.get_invalid_ids(int(start), int(end))
            result += sum(invalid_ids)

        return result

