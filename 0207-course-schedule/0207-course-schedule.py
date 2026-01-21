class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Input  0  to numsCourses-1
        #  prerequisites [[cur,prev]]
        # Output: finish all courses  count==numsCourse
        
        indegree=[0]*numCourses 
        schedule=defaultdict(list)
        # 1. indegree to know how many prev for each course
        # 2. schedule: if one course finish , how many course could reduce one indegree-1
        for cur,prev in prerequisites:
            schedule[prev].append(cur)
            indegree[cur]+=1
        
        q=deque()# prev finish could process
        # indegree[i]==0
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        count=0
        while q:
            prev=q.popleft()
            count+=1
            # schedule map  prev-> [course, course,courese]
            for course in schedule[prev]:
                indegree[course]-=1
                if indegree[course]==0:
                    q.append(course)

        return count==numCourses

