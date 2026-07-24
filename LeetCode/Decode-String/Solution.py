1class Solution:
2    def decodeString(self, s: str) -> str:
3        stack=[]
4        cur=""
5        num=0
6        for c in s:
7            if c.isdigit():
8                num=num*10+int(c)
9            elif c=="[":
10                stack.append((cur,num))
11                cur=""
12                num=0
13            elif c=="]":
14                prev,repeat=stack.pop()
15                cur = prev + repeat * cur
16            else:
17                cur=cur+c
18        
19        return cur
20