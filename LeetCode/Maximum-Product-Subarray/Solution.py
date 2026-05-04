1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        dp_max=[0]*len(nums)
4        dp_min=[0]*len(nums)
5        res = nums[0]
6
7        dp_max[0] = nums[0]
8        dp_min[0] = nums[0] 
9        
10        for i in range(1, len(nums)):
11            dp_max[i] = max(nums[i], nums[i] * dp_max[i-1], nums[i] * dp_min[i-1])
12            dp_min[i] = min(nums[i], nums[i] * dp_max[i-1], nums[i] * dp_min[i-1])
13            res = max(res, dp_max[i])
14        
15        return res