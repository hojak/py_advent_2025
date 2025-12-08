from day6.tools import transpose_text


class CephalopodsMath:

    def __init__(self, content):
        self.transposed_content = transpose_text(content)

    def get_result(self):
        total_result = 0
        multiply = False

        sub_result = 0
        for line in self.transposed_content:
            if (line.strip() == ""):
                total_result += sub_result
                sub_result = 0
                multiply = False
            else:
                if (line[-1] == "*"):
                    multiply = True
                    sub_result = 1

                number_text = line[0:-1].strip()

                if (multiply):
                    sub_result *= int(number_text)
                else:
                    sub_result += int(number_text)

        total_result += sub_result

        return total_result
