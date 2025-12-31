class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def helper(path,left,right):
            if len(path)==n*2:
                res.append(path)
                return 
            if left<n:
                helper(path+"(",left+1,right)
            if right<left:
                helper(path+")",left,right+1)
        helper("",0,0)
        return res