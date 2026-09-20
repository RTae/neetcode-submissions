class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        N = len(grid)

        if grid[0][0] or grid[N-1][N-1]:
            return -1

        visit = set()
        q = deque()
        q.append((0,0,1))
        visit.add((0,0))

        direction = [(0,1), (1,0), (0,-1), (-1,0)]

        while q:
            i,j,minute = q.popleft()
            for di,dj in direction:
                ni, nj = i+di, j+dj
                if (0 <= ni < N and 0 <= nj < N and grid[ni][nj] == 1 and (ni,nj) not in visit):
                    q.append((ni,nj,minute+1))
                    visit.add((ni,nj))
                    
        return -1