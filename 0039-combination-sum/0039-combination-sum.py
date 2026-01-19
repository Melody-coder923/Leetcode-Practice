class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def backtrack(path,start,remain):
            if remain==0:
                res.append(path[:])
                return 
            
            for i in range(start,len(candidates)):
                if candidates[i]>remain:
                    break
                path.append(candidates[i])
                backtrack(path,i,remain-candidates[i])
                path.pop()
        backtrack([],0,target)
        return res