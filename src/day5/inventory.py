class Inventory:
    def __init__(self) -> None:
        self.fresh_ranges = []

    def is_in_range(id: int, range: tuple) -> bool:
        return range[0] <= id <= range[1]

    def find_nearest_smaller_range(self, id: int) -> tuple | None:
        if (len(self.fresh_ranges) == 0 or self.fresh_ranges[0][0] > id):
            return None
        if (self.fresh_ranges[len(self.fresh_ranges) - 1][0] <= id):
            return self.fresh_ranges[len(self.fresh_ranges) - 1]

        left_index = 0
        right_index = len(self.fresh_ranges) - 1

        while left_index < right_index:
            if (left_index + 1 == right_index):
                if (self.fresh_ranges[right_index][0] <= id):
                    left_index = right_index
                else:
                    right_index = left_index

            mid_index = (left_index + right_index + 1) // 2

            if (self.fresh_ranges[mid_index][0] <= id):
                left_index = mid_index
            else:
                right_index = mid_index

        if (self.fresh_ranges[left_index][0] <= id):
            return self.fresh_ranges[left_index]
        else:
            return None

    def is_fresh(self, id: int) -> bool:
        range = self.find_nearest_smaller_range(id)
        return range is not None and Inventory.is_in_range(id, range)

    def add_fresh_id_range(self, start_id: int, end_id: int) -> None:
        index = 0

        while (index < len(self.fresh_ranges) and
               self.fresh_ranges[index][0] < start_id):
            index += 1

        if (index > 0 and self.fresh_ranges[index-1][1] >= start_id):
            self.fresh_ranges[index-1] = (self.fresh_ranges[index-1][0], end_id)
        else:
            self.fresh_ranges.insert(index, (start_id, end_id))
