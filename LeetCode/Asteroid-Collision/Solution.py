1class Solution:
2    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
3        stack=[]
4        for num in asteroids:
5            if num<0:
6                while stack and stack[-1]>0 and stack[-1]<abs(num):
7                    stack.pop()
8                if stack and stack[-1]==abs(num):
9                    stack.pop()
10                    continue 
11                if stack and stack[-1]<0:
12                    stack.append(num)
13                if not stack:
14                    stack.append(num)
15            if num>0:    
16                stack.append(num)
17        return stack 