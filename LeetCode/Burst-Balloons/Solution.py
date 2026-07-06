1class Solution:
2    def maxCoins(self, nums: List[int]) -> int:
3        nums = [1] + nums + [1]
4        n = len(nums)
5
6        @lru_cache(None)
7        def dfs(left,right):
8            if right-left==1:
9                return 0
10            res = 0
11            for k in range(left+1,right):
12                coins= dfs(left,k)+nums[left]*nums[k]*nums[right]+dfs(k,right)
13                res=max(res,coins)
14            return res
15
16        return dfs(0,n-1)
17
18
19