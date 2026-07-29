1class Solution:
2    def smallestSubsequence(self, s: str) -> str:
3        map={}
4        for idx,char in enumerate(s):
5            map[char]=idx
6        
7        seen=set()
8        stack=[]
9        for idx,char in enumerate(s):
10            if char in seen:
11                continue
12
13            # 如果字母出现更小，需要比较
14            # 栈顶更大，并且栈顶字符后面还能找到
15            while (
16                stack
17                and stack[-1] > char
18                and map[stack[-1]] > idx
19            ):
20                removed = stack.pop()
21                seen.remove(removed)
22
23            #如果没有更小呢
24            stack.append(char)
25            seen.add(char)
26
27        return "".join(stack)
28
29            
30
31            
32