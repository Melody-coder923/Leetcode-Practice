class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        parent=list(range(n))
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            root_x=find(x)
            root_y=find(y)
            if root_x==root_y:
                return False
            parent[root_y]=root_x
            return True
        
        for a,b in connections:
            union(a,b)
        
        components = len(set(find(i) for i in range(n)))
        return components-1

        