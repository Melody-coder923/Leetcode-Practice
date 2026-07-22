1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        res=[]
4        n=len(candidates)
5        candidates.sort()
6        def backtrack(start,path,remain):
7            if remain==0:
8                res.append(path[:])
9                return 
10
11            for i in range(start,n):
12                if candidates[i]>remain:
13                    break
14                path.append(candidates[i])
15                backtrack(i,path,remain-candidates[i])
16                path.pop()
17        
18        backtrack(0,[],target)
19
20        return res
21
22                