class Inventory:

    fresh_ranges = []

    def is_in_range(id: int, range: tuple) -> bool:
        return range[0] <= id <= range[1]

    def is_fresh(self, id: int) -> bool:
        for range in self.fresh_ranges:
            if Inventory.is_in_range(id, range):
                return True

        return False

    def add_fresh_id_range(self, start_id: int, end_id: int) -> None:
        self.fresh_ranges.append((start_id, end_id))
