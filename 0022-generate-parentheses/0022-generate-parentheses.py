class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(l,r,path):
            if len(path)==2*n:
                res.append(path)
                return 
            
            if l<n:
                dfs(l+1,r,path+"(")
            if r<l:
                dfs(l,r+1,path+")")
        dfs(0,0,"")

        return res