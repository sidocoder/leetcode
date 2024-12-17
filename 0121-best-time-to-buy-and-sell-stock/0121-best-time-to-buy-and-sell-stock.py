from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        l = 0
        r = l + 1
        profits = 0
        while r < len(prices):
            
            if prices[r] > prices[l]:
                profit =prices[r] - prices[l]
                profits = max(profits,profit)
            else:
                l = r
            r += 1
        return profits
        
       