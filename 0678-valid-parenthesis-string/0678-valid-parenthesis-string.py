class Solution:
    def checkValidString(self, s: str) -> bool:
        stack=[]
        star=[]
        for i, char in enumerate(s):
            if char=="(":
                stack.append(i)
            elif char=="*":
                star.append(i)
            else:
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while stack and star:
            if stack[-1]>star[-1]:
                return False
            stack.pop()
            star.pop()
        return not stack
