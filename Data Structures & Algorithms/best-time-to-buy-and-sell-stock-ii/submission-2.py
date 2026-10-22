class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # dp[i][0] = max profit from day i onward, holding NO shares (flat)
        # dp[i][1] = max profit from day i onward, holding ONE share
        # Base: after the last day, nothing can be earned -> 0
        dp = [[0, 0] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            # Flat: either stay flat, or buy today and move to holding
            dp[i][0] = max(dp[i + 1][0], -prices[i] + dp[i + 1][1])
            # Holding: either keep holding, or sell today and move to flat
            dp[i][1] = max(dp[i + 1][1], prices[i] + dp[i + 1][0])

        # Start on day 0 holding zero shares -> answer is the flat state
        return dp[0][0]