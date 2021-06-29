class SolutionBruteForce:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            subsum = 0
            for j in range(i, n):
                subsum += nums[j]
                if subsum == k:
                    count += 1
                    
        return count


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_cache = {}
        count = 0
        cum_sum = 0
        for num in nums:
            cum_sum += num
            if cum_sum == k:
                count += 1

            count += sum_cache.get(cum_sum - k, 0)
            sum_cache[cum_sum] = sum_cache.get(cum_sum, 0)  + 1
                    
        return count
