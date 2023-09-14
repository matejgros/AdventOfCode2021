def calculate_syntax_error_line(line):
    stack = []  # A stack to keep track of opened chunks
    illegal_characters = {")": 3, "]": 57, "}": 1197, ">": 25137}
    error_score = 0

    for char in line:
        if char in "([{<":
            stack.append(char)
        elif char in ")]}>":
            if not stack or not is_matching_pair(stack.pop(), char):
                error_score += illegal_characters.get(char)
    return error_score


def is_matching_pair(opening, closing):
    pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
    return pairs[opening] == closing


def calculate_total_error_score(input_string):
    input_lines = input_string.splitlines()
    total_error_score = 0

    for line in input_lines:
        total_error_score += calculate_syntax_error_line(line)
    return total_error_score


# Part 2
def find_middle_score(input_string):
    input_lines = input_string.splitlines()
    incomplete_lines = []

    for line in input_lines:
        # We can reuse method from part 1 to find incomplete lines
        if calculate_syntax_error_line(line) == 0:
            incomplete_lines.append(line)
    # First we find the completion string and then we calculate its score
    scores = [calculate_score(complete_line(line)) for line in incomplete_lines]
    sorted_scores = sorted(scores)

    middle_index = len(sorted_scores) // 2
    middle_score = sorted_scores[middle_index]
    return middle_score


def calculate_score(line):
    score = 0
    score_table = {")": 1, "]": 2, "}": 3, ">": 4}
    for char in line:
        score = score * 5 + score_table[char]
    return score


def complete_line(incomplete_line):
    stack = []
    completion_string = ""
    pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
    for char in incomplete_line:
        if char in "({[<":
            stack.append(char)
        elif char in ")}]>":
            if char == pairs[stack[-1]]:
                stack.pop()
    # We need to complete the open paranthesis left on the stack
    while stack:
        completion_string += pairs[stack.pop()]
    return completion_string


if __name__ == "__main__":
    navigation_input_example = """[({(<(())[]>[[{[]{<()<>>
    [(()[<>])]({[<{<<[]>>(
    {([(<{}[<>[]}>{[]{[(<()>
    (((({<>}<{<{<>}{[]{[]{}
    [[<[([]))<([[{}[[()]]]
    [{[{({}]{}}([{[{{{}}([]
    {<[[]]>}<{[{[{[]{()[[[]
    [<(<(<(<{}))><([]([]()
    <{([([[(<>()){}]>(<<{{
    <{([{{}}[<[[[<>{}]]]>[]]"""

    navigation_input = open("day10_input.txt", "r").read()

    # Part 1
    total_error_score = calculate_total_error_score(navigation_input)
    print(f"Total Syntax Error Score: {total_error_score}")

    # Part 2
    middle_score = find_middle_score(navigation_input)
    print(f"Middle Score: {middle_score}")
