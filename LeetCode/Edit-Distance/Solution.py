1class Solution:
2    def minDistance(self, word1: str, word2: str) -> int:
3        #Edge case:
4        m,n= len(word1),len(word2)
5        if m==0:
6            return n
7        if n==0:
8            return m
9
10        @lru_cache(None)
11        def dfs(i,j):
12        #base case:
13            if j<0:
14                return i+1
15            if i<0:
16                return j+1
17            
18            if word1[i]==word2[j]:
19                return dfs(i-1,j-1)
20
21            # word1[i]!=word2[j]
22            delete=dfs(i-1,j)+1
23            insert=dfs(i,j-1)+1
24            replace=dfs(i-1,j-1)+1
25            return min(delete,insert,replace)
26
27        return dfs(m-1,n-1)