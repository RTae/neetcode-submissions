class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        maxArea = 0


        def dfs(r, c, islandSize):
            if r<0 or c<0 or r>=m or c>=n or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            islandSize+=1

            dfs(r+1,c,islandSize)
            dfs(r-1,c,islandSize)
            dfs(r,c+1,islandSize)
            dfs(r,c-1,islandSize)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islandSize = 0
                    dfs(i,j,islandSize)
                    maxArea = max(maxArea, islandSize)

        return maxArea