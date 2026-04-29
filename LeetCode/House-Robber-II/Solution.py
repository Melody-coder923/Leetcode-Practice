1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        #edge case
4        n=len(nums)
5        if n==1:
6            return nums[0]
7        if n==2:
8            return max(nums[0],nums[1])
9        #def dp i 为结尾的最多能投多少
10        # build dp and initialize 
11        def dp_function(arr):
12            n=len(arr)
13            if n==1:
14                return arr[0]
15            if n==2:
16                return max(arr[0],arr[1])
17            dp= [0]* n
18            dp[0]= arr[0]
19            dp[1]=max(arr[0],arr[1])
20            # transition
21            for i in range(2,n):
22                dp[i]= max(dp[i-1],dp[i-2]+arr[i])
23            return dp[-1]
24
25        return max(dp_function(nums[1:]),dp_function(nums[:-1]))