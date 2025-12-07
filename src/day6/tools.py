def transpose_text(input: str) -> list[str]:
    result_lines = []
    
    input_lines = input.splitlines()
    for index in range(0, len(input_lines[0])):
        result_lines.append("")
    
    for line in input_lines:
        for index in range(0, len(line)):
            result_lines[index] += line[index]
            
    return result_lines