1class Solution:
2    def calculate(self, s: str) -> int:
3        stack = []
4        res = 0
5        num = 0
6        sign = 1
7
8        for c in s:
9            if c.isdigit():
10                num = num * 10 + int(c)
11
12            elif c == "+":
13                res += sign * num
14                num = 0
15                sign = 1
16
17            elif c == "-":
18                res += sign * num
19                num = 0
20                sign = -1
21            
22            elif c == "(":
23                stack.append(res)
24                stack.append(sign)
25                res = 0
26                num = 0
27                sign = 1
28
29            elif c == ")":
30                res += sign * num
31                num = 0
32                prev_sign = stack.pop()
33                prev_res = stack.pop()
34                res = prev_res + prev_sign * res
35
36        return res + sign * num