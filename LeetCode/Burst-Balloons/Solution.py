1class Solution:
2    def maxCoins(self, nums: List[int]) -> int:
3        nums=[1]+nums+[1]
4        n=len(nums)
5        dp= [[0]*n for _ in range(n)]
6
7        for length in range(2,n):
8            for left in range(0,n-length):
9                right=left+length
10                for k in range(left+1,right):
11                    coin=dp[left][k] + nums[left] * nums[k] * nums[right] + dp[k][right]
12                    dp[left][right]=max(coin,dp[left][right])
13        return dp[0][n-1]