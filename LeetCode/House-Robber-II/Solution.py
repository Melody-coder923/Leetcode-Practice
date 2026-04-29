1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n=len(nums)
4        #edge case
5        if n==1:
6            return nums[0]
7        if n==2:
8            return max(nums[0],nums[1])
9        
10        def helper(nums):
11            n=len(nums)
12            dp=[0]*n
13
14            dp[0]=nums[0]
15            dp[1]=max(nums[1],nums[0])
16
17            for i in range(2,n):
18                dp[i]=max(dp[i-1],dp[i-2]+nums[i])
19            
20            return dp[n-1]
21        
22        return max(helper(nums[1:]),helper(nums[:-1]))