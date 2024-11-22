class Solution:
    def maximumProfit(self, prices):
        # code here
        min_so_far = float("inf")
        max_profit = 0
        
        for p in prices:
            min_so_far = min(p,min_so_far)
            
            max_profit = max(max_profit,p -min_so_far)

        return max_profit
        
