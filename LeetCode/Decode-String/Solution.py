1class Solution:
2    def decodeString(self, s: str) -> str:
3        stack=[]
4        num=0
5        curr=""
6        cur_num=0
7        res=""
8        for c in s:
9            if c.isdigit():
10                num=num*10+int(c)
11            elif c=="[":
12                stack.append((curr, num))
13                curr=""
14                num=0
15            elif c=="]":
16                prev, repeat = stack.pop()
17                curr = prev + repeat * curr
18            else:
19                curr=curr+c
20
21        return curr
22       