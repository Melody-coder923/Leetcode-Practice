1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        res=[]
4        candidates.sort()
5
6        def backtrack(start,path,remain):
7            if remain==0:
8                res.append(path[:])
9                return 
10            for i in range(start,len(candidates)):
11                if candidates[i]>remain:
12                    break
13                path.append(candidates[i])
14                backtrack(i,path,remain-candidates[i])
15                path.pop()
16
17        backtrack(0, [], target)
18        return res
19
20        