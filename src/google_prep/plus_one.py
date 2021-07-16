from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        N = len(digits)
        carriage = 0
        val = digits[N - 1] + 1
        if val < 10:
            output = list(digits)
            output[N - 1] = val
            return output

        carriage = 1
        output = (N + 1) * [0]
        for i in range(N - 2, -1, -1):
            val = digits[i] + carriage
            if val == 10:
                output[i + 1] == 0
                carriage = 1
            else:
                carriage = 0
                output[i + 1] = val
        if carriage == 1:
            output[0] = 1
            return output
        return output[1:]


sol = Solution()

print(sol.plusOne([4, 3, 2, 1]))
print(sol.plusOne([0]))
print(sol.plusOne([1, 9]))
print(sol.plusOne([9, 9]))
