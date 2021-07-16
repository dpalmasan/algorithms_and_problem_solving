def solution(A, B):
    # Downstream fishes
    stack = []
    survivors = 0
    N = len(A)
    for i in range(N):
        if B[i] == 0:
            survivors += 1
            while stack:
                if stack[-1] > A[i]:
                    survivors -= 1
                    break
                else:
                    stack.pop()
        else:
            stack.append(A[i])
    return survivors + len(stack)


assert solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]) == 2
assert solution([4, 3, 2, 1, 5], [0, 0, 0, 0, 0]) == 5
assert solution([4, 3, 2, 1, 5], [1, 1, 1, 1, 1]) == 5
assert solution([4, 3, 2, 1, 5], [1, 1, 1, 1, 0]) == 1
assert solution([4, 3, 2, 1, 5], [0, 0, 0, 0, 1]) == 5
assert solution([10, 2, 3, 4, 5], [1, 0, 1, 0, 0]) == 1
assert solution([10, 6, 3, 4, 7], [1, 1, 0, 0, 0]) == 1
