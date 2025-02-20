def correct_brackets_sequence(s: str):
    stack = []
    mapping = {
        "(": ")",
        "{": "}",
        "[": "]"
    }

    for bracket in s:
        if bracket in mapping:
            stack.append(bracket)
        else:
            if len(mapping) < 1:
                return False
            elif bracket != mapping[stack.pop()]:
                return False

    return len(stack) == 0


assert correct_brackets_sequence("([])") is True
assert correct_brackets_sequence("{)") is False
assert correct_brackets_sequence("{[()()][]}") is True
