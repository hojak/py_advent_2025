class Circuit():

    def __init__(self, initial_junction_boxes=[]):
        self.junction_boxes = initial_junction_boxes

    def add_junction_box(self, junction_box):
        if (junction_box not in self.junction_boxes):
            self.junction_boxes.append(junction_box)

    def get_size(self):
        return len(self.junction_boxes)

    def get_junction_boxes(self):
        return self.junction_boxes

    def merge_with(self, other_circuit):
        for box in other_circuit.get_junction_boxes():
            self.add_junction_box(box)
