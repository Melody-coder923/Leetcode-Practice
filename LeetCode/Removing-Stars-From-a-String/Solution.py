1class Solution:
2    def removeStars(self, s: str) -> str:
3        stack=[]   
4        for char in s:   
5            if char!= "*":
6                stack.append(char)  
7            else:
8                stack.pop()
9        return "".join(stack)
10