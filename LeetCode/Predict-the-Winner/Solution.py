1class Solution:
2    def predictTheWinner(self, nums: List[int]) -> bool:
3        n=len(nums)
4        dp=[[0] * n for _ in range(n)]
5        #base case
6        for i in range(n):
7            dp[i][i]=nums[i]
8        
9        for length in range(2, n + 1):
10            for l in range(n - length + 1):
11                r = l + length - 1
12                take_left = nums[l] - dp[l + 1][r]
13                take_right = nums[r] - dp[l][r - 1]
14                dp[l][r] = max(take_left, take_right)
15
16        return dp[0][n - 1] >= 0