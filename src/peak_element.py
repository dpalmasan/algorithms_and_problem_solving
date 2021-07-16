"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        b = len(nums) - 1
        a = 0
        while a < b:
            mid = (a + b) // 2
            if nums[mid] > nums[mid + 1]:
                b = mid
            else:
                a = mid + 1
        return a


print(Solution().findPeakElement([1, 2, 3, 1]))
