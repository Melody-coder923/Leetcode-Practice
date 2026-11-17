class Solution:
    def simplifyPath(self, path: str) -> str:
        #split
        lst=path.split("/")
        #stack
        stack=[]

        for s in lst:
            if s=="" or s==".":
                continue

            if s=="..":
                if stack:
                    stack.pop()
                continue        
                
            else:
                stack.append(s)

        # join

        res="/"+"/".join(stack)

        return res
