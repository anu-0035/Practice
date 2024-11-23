from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        n = len(prices)
        if n <= 1:
            return 0
        max_profit = 0
        for i in range(1,n):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit
