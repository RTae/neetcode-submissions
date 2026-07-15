class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        maxArea = 0


        def dfs(r, c):
            if r<0 or c<0 or r>=m or c>=n or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            
            count=1
            count+=dfs(r+1,c)
            count+=dfs(r-1,c)
            count+=dfs(r,c+1)
            count+=dfs(r,c-1)

            return count
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    islandSize = dfs(i,j)
                    maxArea = max(maxArea, islandSize)

        return maxArea