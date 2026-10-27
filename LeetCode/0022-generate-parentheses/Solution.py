class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        total=2*n
        res=[]
        def backtrack(l,r,path):
            if l+r==total:
                res.append("".join(path))
                return 
            
            if l<n:
                path.append("(")
                backtrack(l+1,r,path)
                path.pop()

            if r<l:
                path.append(")")
                backtrack(l,r+1,path)
                path.pop()
            
        backtrack(0,0,[])

        return res