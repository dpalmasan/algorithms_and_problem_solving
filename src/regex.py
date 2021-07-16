MATCH_ANY = "."


def move_pointer(input: str, regex: str, i: int, j: int):
    m = len(input)
    n = len(regex)

    if i == m and j != n:
        return False

    if input[i] == regex[j] or regex[j] == MATCH_ANY:
        if i == m - 1 and j == n - 1:
            return True
        if j < n - 1:
            if regex[j + 1] != "*":
                return move_pointer(input, regex, i + 1, j + 1)
            else:
                return match_star(input, regex, i, j)

    else:
        if j < n - 1 and regex[j + 1] == "*":
            return move_pointer(input, regex, i, j + 2)
        else:
            return False


def match_star(input: str, regex: str, i: int, j: int):
    m = len(input)
    n = len(regex)
    if i == m - 1:
        # If we are at an end state we return True
        if j + 1 == n - 1:
            return True
        else:
            return move_pointer(input, regex, i, j + 2)

    # Consume current input
    if input[i] == regex[j] or regex[j] == MATCH_ANY:
        return match_star(input, regex, i + 1, j)
    return move_pointer(input, regex, i + 1, j + 2)


def match_regex(input: str, regex: str):
    """Check if string matches reges.

    Supported patterns:

    [A-Z]
    . Match any character
    * Match 0 or more of one character

    examples:

    A*B matches B, AB, AAAAB, does not match A

    :param input: [description]
    :type input: str
    :param regex: [description]
    :type regex: str
    :return: [description]
    :rtype: [type]
    """
    return move_pointer(input, regex, 0, 0)


print(match_regex("AAAAAAAAB", "A*A*A*BB"))
print(match_regex("AAAAAAAAB", "A*B"))
print(match_regex("AAAAAAAAB", "A*A*A*B"))
print(match_regex("BA", "A*A*A*BB"))
print(match_regex("CBBA", ".B*A"))
print(match_regex("ASDVASCBBDASDAC", ".*A"))
print(match_regex("ASDVASCBBDASDA", ".*A"))
