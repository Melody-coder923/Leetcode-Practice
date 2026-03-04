1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack=[]
4        map={
5            ')':'(',
6            '}':'{',
7            ']':'['
8        }
9        for c in s:
10            if c in map and stack:
11                if map[c]!=stack.pop():
12                    return False
13            elif c in map and not stack:
14                return False
15            else:
16                stack.append(c)
17        return not stack