class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        fresh=0
        directions=[(1,0),(-1,0),(0,-1),(0,1)]
        q=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j,0))
                elif grid[i][j]==1:
                    fresh+=1

        if fresh==0:
            return 0

        while q:
            size=len(q)
            for _ in range(size):
                x,y,time=q.popleft()
                for dx,dy in directions:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1:
                        grid[nx][ny] = 2
                        q.append((nx,ny,time+1))
                        fresh-=1
                        if fresh==0:
                            return time+1    
                            
        if fresh!=0:
            return -1