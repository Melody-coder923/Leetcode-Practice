class Solution:
    def countCollisions(self, directions: str) -> int:
        # 情况1: R,L
        # 情况2: R/L OR S
        # 情况3: R持续往右开

        res=0
        stack=[directions[0]]

        for c in directions[1:]:
            if stack[-1]=="R" and c=="L":
                res+=2
                stack.pop()
                c="S"
            elif stack[-1]=="S" and c=="L":
                res+=1
                c="S"
            while stack and (stack[-1]=="R" and c=="S"):
                res+=1
                stack.pop()
            
            stack.append(c)

        return res
                
            