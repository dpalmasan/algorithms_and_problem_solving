def solution(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack:
                return 0
            else:
                stack.pop()
    return len(stack) == 0


assert solution("(()(())())")
assert not solution("())")
assert solution("")
assert solution("()")
assert not solution("(((((((((()")
