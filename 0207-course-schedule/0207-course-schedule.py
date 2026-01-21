class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        schedule=defaultdict(list)
        indegree=[0]*numCourses
        for pre,cur in prerequisites:
            schedule[pre].append(cur)
            indegree[cur]+=1
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        count=0
        while q:
            prev= q.popleft()
            count+=1
            for cur in schedule[prev]:
                indegree[cur]-=1
                if indegree[cur]==0:
                    q.append(cur)
                    
        return count==numCourses