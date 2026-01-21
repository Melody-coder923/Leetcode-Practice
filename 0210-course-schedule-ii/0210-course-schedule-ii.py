class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree=[0]*numCourses
        schedule=defaultdict(list)
        for cur,prev in prerequisites:
            schedule[prev].append(cur)
            indegree[cur]+=1
        
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        res=[]
        while q:
            prev=q.popleft()
            res.append(prev)
        
            for cur in schedule[prev]:
                indegree[cur]-=1
                if indegree[cur]==0:
                    q.append(cur)
        
        return res if len(res)==numCourses else []