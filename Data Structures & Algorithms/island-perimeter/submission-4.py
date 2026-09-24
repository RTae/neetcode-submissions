class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Apply DFS into a problem
        # We need to check that there is a island next to
        # the focus island or not and then using DFS to spread
        # then track it by using visit variable

        row, col = len(grid), len(grid[0])
        # track visit island
        visit = set()

        def dfs(i,j):
            # make sure it's not exceed gird and found a water
            # then count 1
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == 0:
                return 1
            # it's already visit
            if (i,j) in visit:
                return 0
            
            visit.add((i,j))

            count = dfs(i,j+1) + dfs(i+1,j) + dfs(i,j-1) + dfs(i-1,j)
            return count
        
        # Loop check each grid
        for i in range(row):
            for j in range(col):
                # if it's a island 
                if grid[i][j]:
                    return dfs(i,j)

        return 0