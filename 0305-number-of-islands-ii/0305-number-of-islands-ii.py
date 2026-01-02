class DSU:
    def __init__(self):
        self.parent={}
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        root_x=self.find(x)
        root_y=self.find(y)
        if root_x==root_y:
            return False
        self.parent[root_y]=root_x
        return True

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        dsu=DSU()
        land=set()
        res=[]
        count=0
        for i, j in positions:
            if (i,j) in land:
                res.append(count)
                continue
            land.add((i,j))
            dsu.parent[(i,j)]=(i,j)
            count+=1
            directions=[(0,1),(0,-1),(1,0),(-1,0)]
            for dx,dy in directions:
                nx,ny=i+dx,j+dy
                if (nx,ny) in land:
                    if dsu.union((nx,ny),(i,j)) :
                        count-=1
            res.append(count)
        return res

