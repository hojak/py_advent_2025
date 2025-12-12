import re


def read_from_file(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    return content


def split_lines_into_numbers(text_file_input: str) -> list:
    return list(map(lambda line: [int(string) for string in re.split('\\s+', line)], text_file_input.split('\n')))


def replace_char_at(string: str, index: int, new_char: str) -> str:
    return string[:index] + new_char + string[index + 1:]
