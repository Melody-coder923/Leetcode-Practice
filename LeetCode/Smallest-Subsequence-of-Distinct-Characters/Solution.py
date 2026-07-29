1class Solution:
2    def smallestSubsequence(self, s: str) -> str:
3        map={}
4        
5        for idx,c in enumerate(s):
6            map[c]=idx
7        
8        stack=[]
9        seen=set()
10        for idx,char in enumerate(s):
11            if char in seen:
12                continue
13            while stack and stack[-1]>char and map[stack[-1]]>idx:
14                removed=stack.pop()
15                seen.remove(removed)
16            
17            #如果没有更小呢
18            stack.append(char)
19            seen.add(char)
20        
21        return "".join(stack)