1class Solution:
2    def smallestSubsequence(self, s: str) -> str:
3
4        def can_cover(remain,need):
5            remain_chars=set(remain)
6            return need.issubset(remain_chars)
7        
8        def dfs(remain,still_need):
9            if not still_need:
10                return ""
11    
12            for char in sorted(still_need):
13                idx=remain.find(char)
14                next_need = still_need - {char} #必须新建
15                if can_cover(remain[idx+1:],next_need):
16                   return char+dfs(remain[idx+1:],next_need)
17        
18        return dfs(s,set(s))
19