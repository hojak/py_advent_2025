class Playground:

    def __init__(self):
        self.junction_boxes = []

    def add_junction_box(self, junction_box):
        self.junction_boxes.append(junction_box)

    def number_of_boxes(self) -> int:
        return len(self.junction_boxes)
