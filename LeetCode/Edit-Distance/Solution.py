1class Solution:
2    def minDistance(self, word1: str, word2: str) -> int:
3        m,n=len(word1),len(word2)
4        #edge case
5        if not word1:
6            return n
7        if not word2:
8            return m
9        @lru_cache(None)
10        def dfs(i,j):
11            if i < 0:
12                return j + 1  
13            if j < 0:
14                return i + 1  
15
16            if word1[i] == word2[j]:
17                return dfs(i - 1, j - 1)
18
19            # 三种操作都要 +1
20            replace_cost = dfs(i - 1, j - 1) + 1
21            delete_cost  = dfs(i - 1, j) + 1
22            insert_cost  = dfs(i, j - 1) + 1
23            return min(replace_cost, delete_cost, insert_cost)
24
25        return dfs(m - 1, n - 1)