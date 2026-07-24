class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])

        # Block both start and destination, so path is impossible
        if obstacleGrid[0][0] == 1 or obstacleGrid[M-1][N-1] == 1:
            return 0

        # Create init table
        dp = [[0] * (N+1) for _ in range(M+1)]
        # keep track from ending
        dp[M-1][N-1] = 1

        # start at the end and then keep step down unit reach starting point
        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                # if the current path is block, so it's mean we cannot cross
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] += dp[i+1][j] + dp[i][j+1]

        
        return dp[0][0]