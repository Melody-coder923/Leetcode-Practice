class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # step1: 求岛屿面积, 编号
        n=len(grid)
        island={} #key: island_id -> 面积
        def cal(island_id,x,y):
            if x<0 or x>=n or y<0 or y>=n or grid[x][y]!=1:
                return 0
            grid[x][y]=island_id
            return cal(island_id,x+1,y)+cal(island_id,x-1,y)+cal(island_id,x,y+1)+cal(island_id,x,y-1)+1

        island_id=2
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    island[island_id]=cal(island_id,i,j)
                    island_id+=1

        # step2: 以0为中心辐射,看看哪个0连接后岛屿面积最大 -max
        def search(x,y):
            area=0
            seen=set()
            directions=[(1,0),(-1,0),(0,1),(0,-1)]
            for dx,dy in directions:
                nx,ny= x+dx,y+dy
                if 0<=nx<n and 0<=ny<n:
                    island_id=grid[nx][ny]
                    if island_id>1 and island_id not in seen:
                        area+=island[island_id]
                        seen.add(island_id)
            return area

        maxarea= max(island.values() or [0])
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    maxarea=max(maxarea,search(i,j)+1)
        return maxarea