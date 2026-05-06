1class Solution:
2    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
3        m,n=len(text1),len(text2)
4        @lru_cache(None)
5        def dfs(i,j):
6            if i==0 or j==0:
7                return 0
8            if text1[i-1]==text2[j-1]:
9                return dfs(i-1,j-1)+1
10            
11            else:
12                return max(dfs(i-1,j),dfs(i,j-1))
13        
14        return dfs(m,n)
15        