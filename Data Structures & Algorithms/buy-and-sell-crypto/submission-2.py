class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Apply DP to buy lowest price and sell at max profit

        maxProfit = 0
        hold = prices[0]

        for sell in prices:
            # compare this give better profit
            maxProfit = max(maxProfit, sell - hold)
            # and check if this is lowest hold
            hold = min(hold, sell)
        
        return maxProfit