class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M,N = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        time = 0
        
        direction = [(0,1), (1,0), (0,-1), (-1,0)]


        # Find where to start to spread
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((r,c))

        while fresh > 0 and q:
            length = len(q)
            for _ in range(length): 
                r,c = q.popleft()

                for dr, dc in direction:
                    row, col = r+dr, c+dc

                    # still in range and fresh
                    if (row in range(M)) and (col in range(N)) and grid[row][col] == 1:
                        # make oit rot
                        grid[row][col] = 2
                        q.append((row,col))
                        fresh -= 1
            time +=1

        return time if fresh == 0 else -1