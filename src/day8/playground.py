from day8.circuit import Circuit


class Playground:

    def __init__(self):
        self.junction_boxes = []
        self.pairs = []
        self.circuits = []

    def add_junction_box(self, junction_box):
        self.pairs = []
        self.junction_boxes.append(junction_box)
        self.circuits.append(Circuit([junction_box]))

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

        self.pairs.sort(key=lambda pair: pair[0].distance_to(pair[1]))

    def get_circuits(self) -> list:
        return self.circuits

    def connect_boxes(self, box_a, box_b):
        circuit_of_a = self.find_circuit_containing(box_a)
        circuit_of_b = self.find_circuit_containing(box_b)

        if (circuit_of_a != circuit_of_b):
            circuit_of_a.merge_with(circuit_of_b)
            self.circuits.remove(circuit_of_b)

    def find_circuit_containing(self, junction_box) -> Circuit:
        for circuit in self.circuits:
            if junction_box in circuit.get_junction_boxes():
                return circuit
        return None
