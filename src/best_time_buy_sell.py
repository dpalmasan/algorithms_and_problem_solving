class SolutionNaive:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        best_profit = 0
        for i in range(n):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                if profit > best_profit:
                    best_profit = profit
        return best_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        differences = [0] * len(prices)

        for i in range(1, len(differences)):
            differences[i] = prices[i] - prices[i - 1]

        buy, sell = 0, 0
        max_sum = float("-inf")
        cur_sum = 0
        cur_buy = 0
        for i, diff in enumerate(differences):
            cur_sum += diff
            if cur_sum > max_sum:
                max_sum = cur_sum
                sell = i
                buy = cur_buy
            if cur_sum < 0:
                cur_buy = i + 1
                cur_sum = 0
        if max_sum <= 0:
            return 0
        return prices[sell] - prices[max(buy - 1, 0)]