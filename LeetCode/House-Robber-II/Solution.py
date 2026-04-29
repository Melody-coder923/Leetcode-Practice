1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n=len(nums)
4        #edge case
5        if len(nums)==1:
6            return nums[0]
7        
8        @lru_cache(None)
9        def dfs(i,start):
10            if i<start:
11                return 0
12            
13            return max(
14                nums[i] + dfs(i - 2, start),
15                dfs(i - 1, start)
16            )
17
18        return max(
19            dfs(n - 2, 0),  # 只看 0 到 n-2
20            dfs(n - 1, 1)   # 只看 1 到 n-1
21        )