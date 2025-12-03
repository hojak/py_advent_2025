from math import floor


class IdValidator:  

    def is_valid(some_id) -> bool:
        if (isinstance(some_id, int)):
            some_id = str(some_id)
            
        half = floor(len(some_id) / 2)
        return len(some_id) % 2 != 0 or some_id[:half] != some_id[half:]
