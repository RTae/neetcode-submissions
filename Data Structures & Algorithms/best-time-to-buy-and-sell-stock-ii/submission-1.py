class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # the idea is using dp to solved a issue
        n = len(prices)
        # create a table that give max profit for buying at index 0
        # create a table that give max profit for selling at index 1 
        dp = [[0]*2 for _ in range(n+1)]

        # we run form last day to first day
        for i in range(n-1, -1, -1):
            # compare between next day with a buy i day, since we buy the sign need to be negative
            dp[i][0]=max(dp[i+1][0], -prices[i] + dp[i+1][1])
            # compare between next day with a sell i day
            dp[i][1]=max(dp[i+1][1], prices[i]+dp[i+1][0])

        return dp[0][0]