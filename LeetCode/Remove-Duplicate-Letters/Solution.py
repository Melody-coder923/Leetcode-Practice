1class Solution:
2    def removeDuplicateLetters(self, s: str) -> str:
3        last={}
4        for i,c in enumerate(s):
5            last[c]=i
6        
7        seen=set()
8        stack=[]
9        for i,c in enumerate(s):
10            if c in seen:
11                continue
12            while stack and stack[-1]>c and last[stack[-1]]>i:
13                removed=stack.pop()
14                seen.remove(removed)
15            stack.append(c)
16            seen.add(c)
17        
18        return "".join(stack)
19            