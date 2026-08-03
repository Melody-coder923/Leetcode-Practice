1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        # course,pre_course
4        dict=defaultdict(list)
5        indegree=[0]*numCourses
6        for course,pre_course in prerequisites:
7            dict[pre_course].append(course)
8            indegree[course]+=1
9        
10        q=deque()
11        for course_no in range(numCourses):
12            if indegree[course_no]==0:
13                q.append(course_no)
14
15        count=0
16        while q:
17            cur=q.popleft()
18            count+=1
19            if count==numCourses:
20                return True
21            for nxt in dict[cur]:
22                indegree[nxt]-=1
23                if indegree[nxt]==0:
24                    q.append(nxt)
25
26        return count==numCourses
27
28        
29