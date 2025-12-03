from math import floor


class IdValidator:  

    def is_valid(some_id) -> bool:
        if (isinstance(some_id, int)):
            some_id = str(some_id)
            
        half = floor(len(some_id) / 2)
        return len(some_id) % 2 != 0 or some_id[:half] != some_id[half:]

    def get_invalid_ids(start: int, end: int) -> list:
        result = []
        for id in range(start, end+1):
            if (not IdValidator.is_valid(id)):
                result.append(id)
        return result
