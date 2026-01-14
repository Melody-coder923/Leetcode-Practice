class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        total=n*2
        res=[]
        def helper(l,r,path):
            if l+r==total:
                res.append("".join(path))
                return 
            if l<n:
                path.append("(")
                helper(l+1,r,path)
                path.pop()
            if l>r:
                path.append((")"))
                helper(l,r+1,path)
                path.pop()
        helper(0,0,[])
        return res