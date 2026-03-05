1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack=[]
4        map={
5            ')':'(',
6            '}':'{',
7            ']':'['
8        }
9        for c in s:
10            if c in map:
11                if stack:
12                    if map[c]!=stack.pop():
13                        return False
14                else:
15                    return False
16            else:
17                stack.append(c)
18        return not stack
19                