from typing import List


class SolutionNaive:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        sols = set()
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    a1 = min(nums[i], nums[j], nums[k])
                    a3 = max(nums[i], nums[j], nums[k])
                    a2 = sum((nums[i], nums[j], nums[k])) - (a3 + a1)
                    cand = (a1, a2, a3)
                    if sum(cand) == 0:
                        sols.add(cand)
        return [list(sol) for sol in sols]


class SolutionBinary:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        sorted_nums = sorted(nums)
        sols = set()
        for i, x in enumerate(sorted_nums):
            for j in range(len(nums)):
                if i == j:
                    continue
                a = j
                b = len(nums) - 1
                found = False
                while a < b:
                    mid = (a + b) // 2
                    y = sorted_nums[mid] + sorted_nums[j]
                    if y > -x:
                        b = mid - 1
                    elif y < -x:
                        a = mid + 1
                    else:
                        found = True
                        break
                if found:
                    a1 = min(x, sorted_nums[j], sorted_nums[mid])
                    a3 = max(x, sorted_nums[j], sorted_nums[mid])
                    a2 = sum((x, sorted_nums[j], sorted_nums[mid])) - (a3 + a1)
                    sols.add((a1, a2, a3))
        return [list(sol) for sol in sols]


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        sols = set()
        solved_x = set()
        for i, x in enumerate(nums):
            if x in solved_x:
                continue
            candidates = set()
            for j in range(len(nums)):
                if i == j:
                    continue
                if -x - nums[j] in candidates:
                    a1 = min(x, -x - nums[j], nums[j])
                    a3 = max(x, -x - nums[j], nums[j])
                    a2 = sum((x, -x - nums[j], nums[j])) - (a3 + a1)
                    sols.add((a1, a2, a3))
                candidates.add(nums[j])
            solved_x.add(x)

        return [list(sol) for sol in sols]


sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
print(sol.threeSum([]))
print(sol.threeSum([0]))
print(sol.threeSum([-1, 0, 1]))
print(sol.threeSum([1, 2, -2, -1]))
print(sol.threeSum([-1, 0, 1, 0]))
