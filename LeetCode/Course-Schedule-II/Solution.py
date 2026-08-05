1class Solution:
2    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
3        dict=defaultdict(list)
4        indegree=[0]*numCourses
5        for cur,pre in prerequisites:
6            dict[pre].append(cur)
7            indegree[cur]+=1
8        
9        q=deque()
10        for course in range(numCourses):
11            if indegree[course]==0:
12                q.append(course)
13        res=[]
14        while q:
15            cur=q.popleft()
16            res.append(cur)
17            for nxt in dict[cur]:
18                indegree[nxt]-=1
19                if indegree[nxt]==0:
20                    q.append(nxt)
21        
22        if len(res)!=numCourses:
23            return []
24        return res