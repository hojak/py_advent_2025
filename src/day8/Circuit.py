class Curcuit():

    def __init__(self, initial_junction_boxes=[]):
        self.junction_boxes = initial_junction_boxes

    def add_junction_box(self, junction_box):
        if (self.junction_boxes.index(junction_box) == -1):
            self.junction_boxes.append(junction_box)

    def get_size(self):
        return len(self.junction_boxes)

    def get_junction_boxes(self):
        return self.junction_boxes