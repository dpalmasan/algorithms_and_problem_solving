def max_subarray(array):
    n = len(array)
    low = 0
    high = 0
    max_sum = array[0]
    for i in range(n):
        curr_sum = array[i]
        if curr_sum >= max_sum:
            max_sum = curr_sum
            low = i
            high = i
        for j in range(i + 1, n):
            curr_sum += array[j]
            if curr_sum > max_sum or (
                curr_sum == max_sum and j - i < high - low
            ):
                low = i
                high = j
                max_sum = curr_sum

    return low, high, max_sum


def max_crossing_subarray(array, low, high, mid):
    left_sum = float("-Inf")
    max_left = low
    curr_sum = 0
    for i in range(mid, low - 1, -1):
        curr_sum += array[i]
        if curr_sum > left_sum:
            max_left = i
            left_sum = curr_sum

    right_sum = float("-Inf")
    max_right = high
    curr_sum = 0
    for i in range(mid + 1, high + 1):
        curr_sum += array[i]
        if curr_sum > right_sum:
            max_right = i
            right_sum = curr_sum
    return max_left, max_right, left_sum + right_sum


def max_subarray_recursive(array, low, high):
    if low == high:
        return low, high, array[low]
    mid = (low + high) // 2
    left_low, left_high, left_sum = max_subarray_recursive(array, low, mid)
    right_low, right_high, right_sum = max_subarray_recursive(
        array, mid + 1, high
    )
    cross_low, cross_high, cross_sum = max_crossing_subarray(
        array, low, high, mid
    )

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    if right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    return cross_low, cross_high, cross_sum


def max_subarray_divide_and_conquer(array):
    return max_subarray_recursive(array, 0, len(array) - 1)


def max_subarray_linear(numbers):
    """Find a contiguous subarray with the largest sum."""
    best_sum = float("-inf")
    best_start = best_end = 0  # or: None
    current_sum = 0
    for current_end, x in enumerate(numbers):
        if current_sum <= 0:
            # Start a new sequence at the current element
            current_start = current_end
            current_sum = x
        else:
            # Extend the existing sequence with the current element
            current_sum = max(current_sum + x, x)

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = current_end

    return best_start, best_end, best_sum


# a = [1, -4, 5, 1, -3]
a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
a = [-4, -5, -4, 2, -7]
print(max_subarray(a))
print(max_subarray_divide_and_conquer(a))
print(max_subarray_linear(a))
