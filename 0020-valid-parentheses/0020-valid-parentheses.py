class Solution:
    def isValid(self, s: str) -> bool:
        map={")":"(", "}":"{","]":"["}
        stack=[]
        for c in s:
            if c not in map:
                stack.append(c)
            else:
                if not stack or stack.pop()!= map[c]:
                    return False
        return not stack
                    


