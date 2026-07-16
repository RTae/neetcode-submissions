class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)

        if grid[0][0] or grid[N-1][N-1]:
            return -1

        visit = set()
        q = deque()
        q.append((0,0,1))
        visit.add((0,0))

        direct = [(0, 1), (1, 0), (0, -1), (-1, 0),
                  (1, 1), (-1, -1), (1, -1), (-1, 1)]

        while q:
            i,j,length = q.popleft()
            
            if i == N-1 and j == N-1:
                return length
            
            for di, dj in direct:
                ni, nj = i+di, j+dj
                if(0 <= ni < N and 0 <= nj < N and grid[ni][nj]==0 and (ni,nj) not in visit):
                    q.append((ni,nj,length+1))
                    visit.add((ni,nj))
        
        return -1