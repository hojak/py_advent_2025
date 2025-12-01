class SafeDial:
    SIZE_OF_WHEEL = 100

    position: int = 50

    def __init__(self):
        pass

    def rotate(self, amount: int):
        self.position = (self.position + amount) % SafeDial.SIZE_OF_WHEEL

    def instruction_to_rotation(instruction: str) -> int:
        direction = instruction[0]
        amount = int(instruction[1:])

        if (direction == 'R'):
            return amount
        elif (direction == 'L'):
            return -amount
        else:
            raise ValueError(f"Invalid direction: {direction}")
        
    def instructions_to_number_sequence(instructions: str) -> list[int]:
        dial = SafeDial()
        positions = [dial.position]

        for line in instructions.splitlines():
            rotation = SafeDial.instruction_to_rotation(line)
            dial.rotate(rotation)
            positions.append(dial.position)

        return positions
    
    def get_code_from_sequence(positions: list[int]) -> int:
        return len(list(filter(lambda x: x == 0, positions)))
