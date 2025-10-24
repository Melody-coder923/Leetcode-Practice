class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def backtrack(i,path):
            if i==len(s):
                res.append("".join(path)) 
                return 
            if s[i].isdigit():
                path.append(s[i])
                backtrack(i+1,path)
                path.pop()
            else:
                path.append(s[i].lower())
                backtrack(i+1,path)
                path.pop()

                path.append(s[i].upper())
                backtrack(i+1,path)
                path.pop()
        backtrack(0,[])
        return res