from day6.tools import transpose_text


class CephalopodsMath:

    def __init__(self, content):
        self.transposed_content = transpose_text(content)

    def get_result(self):
        total_result = 0

        for line in self.transposed_content:
            number_text = line[0:-1].strip()
            total_result += int(number_text)

        return total_result
