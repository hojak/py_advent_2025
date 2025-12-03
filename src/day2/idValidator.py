from math import floor


class IdValidator:

    def is_valid(self, some_id) -> bool:
        if (isinstance(some_id, int)):
            some_id = str(some_id)

        half = floor(len(some_id) / 2)
        return len(some_id) % 2 != 0 or some_id[:half] != some_id[half:]

    def get_invalid_ids(start: int, end: int) -> list:
        self = IdValidator()

        result = []
        for id in range(start, end+1):
            if (not self.is_valid(id)):
                result.append(id)
        return result

    def get_checksum(input: str) -> int:
        result = 0
        ranges = input.split(",")
        for range in ranges:
            (start, end) = range.split("-")
            invalid_ids = IdValidator.get_invalid_ids(int(start), int(end))
            result += sum(invalid_ids)

        return result

