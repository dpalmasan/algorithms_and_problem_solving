from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter: Counter = Counter(nums)

        return [el for el, _ in counter.most_common(k)]
