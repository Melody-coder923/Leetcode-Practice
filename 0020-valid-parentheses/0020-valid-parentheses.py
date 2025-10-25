class Solution:
    def isValid(self, s: str) -> bool:
        map={")":"(", "}":"{","]":"["}
        stack=[]
        for c in s:
            if c in map:
                if not stack:
                    return False
                check=stack.pop()
                if check==map[c]:
                    continue
                else:
                    return False
            stack.append(c) #(
        return not stack

