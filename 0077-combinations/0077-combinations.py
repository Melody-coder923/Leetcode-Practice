class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:     
        res=[]
        def backtrack(start,path):
            # base case:
            if len(path)==k:
                res.append(path[:])
                return 
            for i in range(start, n-(k-len(path))+2):
                # n-i+1>=k-len(path) ->i <= n-(k-len(path))+1
                path.append(i)
                backtrack(i+1,path)
                path.pop()
        backtrack(1,[])
        return res