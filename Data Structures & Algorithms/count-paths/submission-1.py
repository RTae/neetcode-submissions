class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(n+1) for i in range(m+1)]

        for i in range(m):
            for j in range(n):
                dp[i][j] += dp[i+1][j] + dp[i][j+1]

        return dp[m][n]