class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Apply DFS to search or adjcent island
        # 1. track vist
        # 2. Apply DFS on 4 direction
        # we will count when exceed or found a water, since we want to count a perimeter, so 4 side wall is needed
        # since it's a conntect island, so we just need to loop find first island

        row, col = len(grid), len(grid[0])
        visit = set()

        def dfs(i, j):
            # found water or exceed grid
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == 0:
                return 1
            # already visit
            if (i,j) in visit:
                return 0
            
            # track visit
            visit.add((i,j))
            # check four direction
            count = dfs(i,j+1) + dfs(i+1,j) + dfs(i,j-1) + dfs(i-1,j)
            return count
        
        for i in range(row):
            for j in range(col):
                # Found island
                if grid[i][j]:
                    return dfs(i,j)
        
        # there is no island
        return 0
