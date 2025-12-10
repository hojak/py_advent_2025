class Playground:

    def __init__(self):
        self.junction_boxes = []
        self.pairs = []

    def add_junction_box(self, junction_box):
        self.pairs = []
        self.junction_boxes.append(junction_box)

    def number_of_boxes(self) -> int:
        return len(self.junction_boxes)

    def get_closest_pair(self, index) -> tuple:
        if (self.pairs == []):
            self.init_pairs()

        return self.pairs[index]

    def init_pairs(self):
        self.pairs = []
        for first in range(0, len(self.junction_boxes)-1):
            for second in range(first+1, len(self.junction_boxes)):
                self.pairs.append((
                    self.junction_boxes[first],
                    self.junction_boxes[second]
                ))
                
        print(self.pairs)
                
        self.pairs.sort(key=lambda pair: pair[0].distance_to(pair[1]))
        
        print(self.pairs)
