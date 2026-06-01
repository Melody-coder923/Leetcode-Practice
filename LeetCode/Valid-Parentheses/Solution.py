1class Solution:
2    def isValid(self, s: str) -> bool:
3        map= { 
4            ")":"(",
5            "]":"[",
6            "}":"{"
7        }
8
9        stack=[]
10        for char in s:
11            if char not in map:
12                stack.append(char) 
13            else:
14                if stack:
15                    if map[char]!= stack.pop():
16                        return False
17                elif not stack:
18                    return False
19        
20        return not stack
21