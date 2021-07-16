from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # Pre-cache distances, min possible distance is 1
        max_dist = 1
        N = len(seats)

        # Naive solution
        for i in range(N):
            if seats[i] == 0:
                if i == 0:
                    dist = 0
                    k = i
                    while k < N and seats[k] == 0:
                        k += 1
                        dist += 1
                elif i == N - 1:
                    dist = 0
                    k = i
                    while k > 0 and seats[k] == 0:
                        k -= 1
                        dist += 1
                else:
                    left_dist = 0
                    k = i
                    while k > 0 and seats[k] == 0:
                        left_dist += 1
                        k -= 1

                    right_dist = 0
                    k = i
                    while k < N and seats[k] == 0:
                        right_dist += 1
                        k += 1
                    dist = min(left_dist, right_dist)

                if dist > max_dist:
                    max_dist = dist
        return max_dist


sol = Solution()
assert sol.maxDistToClosest([0, 1]) == 1
assert sol.maxDistToClosest([1, 0, 0, 0, 1, 0, 1]) == 2
assert sol.maxDistToClosest([1, 0, 0, 0]) == 3
assert sol.maxDistToClosest([0, 0, 1, 0]) == 2
assert sol.maxDistToClosest([0, 0, 0, 0, 1, 0, 1]) == 4
