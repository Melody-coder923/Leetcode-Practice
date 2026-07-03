1class Solution:
2    def maxCoins(self, nums: List[int]) -> int:
3        nums = [1] + nums + [1]
4        n = len(nums)
5
6        @lru_cache(None)
7        def dfs(left, right):
8            # left 和 right 中间没有气球
9            if right - left <= 1:
10                return 0
11
12            res = 0
13
14            # 枚举最后戳爆的气球 k
15            for k in range(left + 1, right):
16                coin = (
17                    dfs(left, k)
18                    + nums[left] * nums[k] * nums[right]
19                    + dfs(k, right)
20                )
21                res = max(res, coin)
22
23            return res
24
25        return dfs(0, n - 1)
26