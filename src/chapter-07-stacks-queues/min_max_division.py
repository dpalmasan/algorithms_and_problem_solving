def valid_block(K, max_sum, A):
    block_sum = 0
    block_count = 0

    for item in A:
        # Check if block commits with the candidate
        if block_sum + item <= max_sum:
            block_sum += item
        else:
            block_sum = item
            block_count += 1

        # If we haven't finished but found K blocks, invalid
        if block_count >= K:
            return False
    return True


def solution(K, M, A):
    lower_bound = max(A)
    upper_bound = sum(A)

    # Corner cases
    if K == 1:
        return upper_bound
    if K > len(A):
        return lower_bound

    while lower_bound <= upper_bound:
        min_max_candidate = (lower_bound + upper_bound) // 2
        if valid_block(K, min_max_candidate, A):
            upper_bound = min_max_candidate - 1
        else:
            lower_bound = min_max_candidate + 1
    return lower_bound


assert solution(3, 5, [2, 1, 5, 1, 2, 2, 2]) == 6
