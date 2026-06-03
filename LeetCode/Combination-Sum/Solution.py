1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        res=[]
4        candidates.sort()
5        def backtrack(start,path, remain):
6            if remain==0:
7                res.append(path[:])
8                return 
9            for i in range(start, len(candidates)):
10                if candidates[i]> remain:
11                    break
12                path.append(candidates[i])
13                backtrack(i, path, remain - candidates[i])
14                path.pop()
15        backtrack(0, [], target)
16        return res