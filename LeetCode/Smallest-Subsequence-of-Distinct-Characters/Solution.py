1class Solution:
2    def smallestSubsequence(self, s: str) -> str:
3        # map 字母对应的位置（取最后出现的位置）
4        map={}
5        
6        for idx,char in enumerate(s):
7            map[char]=idx
8        
9        # stack + seen={}
10        stack=[]
11        seen=set()
12        for idx,char in enumerate(s):
13            if char in seen:
14                continue
15            
16            while stack and stack[-1]>char and map[stack[-1]]>idx:
17                removed=stack.pop()
18                seen.remove(removed)
19            
20            stack.append(char)
21            seen.add(char)
22        
23        return "".join(stack)