1class Solution:
2    def smallestSubsequence(self, s: str) -> str:
3        n=len(s)
4        if n==1:
5            return s
6        last={}
7        for idx,char in enumerate(s):
8            last[char]=idx
9
10        stack=[]
11        seen=set()
12        for idx,char in enumerate(s):
13            if char in seen:
14                continue
15            while stack and stack[-1]>char and last[stack[-1]]>idx:
16                removed=stack.pop()
17                seen.remove(removed)
18            
19            stack.append(char)
20            seen.add(char)
21        
22        return "".join(stack)
23            