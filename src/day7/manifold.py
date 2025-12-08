class Manifold:

    def __init__(self, layout: str):
        self.initial_layout = layout

    def fire_beam(self):
        self.beam_layout = self.initial_layout

    def get_beam_layout(self) -> str:
        return self.beam_layout
    
    def get_number_of_splitted_beams(self) -> int:
        return 0
