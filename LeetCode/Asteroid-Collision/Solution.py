1class Solution:
2    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
3        stack=[]
4
5        for s in asteroids:
6            if s>0:
7                stack.append(s)
8            else:
9                while stack and stack[-1] > 0 and abs(s) > stack[-1]:
10                    stack.pop()
11                if stack and stack[-1] > 0 and abs(s) == stack[-1]:
12                    stack.pop()
13                elif not stack or stack[-1] < 0:
14                    stack.append(s)
15
16        return stack
17    