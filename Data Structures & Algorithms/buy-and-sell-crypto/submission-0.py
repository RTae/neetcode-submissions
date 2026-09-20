class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # apply siding window method
        profit = 0
        hold = prices[0]
        for p in prices:
            if p-hold > profit:
                profit = p-hold
        
        return profit