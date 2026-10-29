class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        parents=[i for i in range(n)]

        def find(i):
            if i!=parents[i]:
                parents[i]=find(parents[i])
            return parents[i]

        def union(i,j):
            root_i=find(i)
            root_j=find(j)

            if root_i==root_j:
                return False
            else:
                parents[root_j]=root_i
                return True

        #不连：
        for u,v in edges:
            if union(u,v): #false connected    # true: not connected -1
                n-=1
        
        return n
                