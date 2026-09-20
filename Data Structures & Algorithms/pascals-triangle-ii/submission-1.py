class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1]*(i+1) for i in range(rowIndex)]

        for i in range(rowIndex):
            for j in range(1,i):
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

        return dp[rowIndex-1][0]