class Solution:
    def simplifyPath(self, path: str) -> str:
        all=path.split("/")
        stack=[]
        for char in all:
            if char=="..":
                if stack:
                    stack.pop()
            elif char!="." and char!="":
                stack.append(char)
        return "/"+"/".join(stack)