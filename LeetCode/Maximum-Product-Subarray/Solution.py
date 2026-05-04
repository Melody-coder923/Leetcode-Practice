1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        cur_max=nums[0]
4        cur_min=nums[0]
5        res=nums[0]
6
7        for i in range(1,len(nums)):
8            temp_max = cur_max 
9            cur_max=max(nums[i],cur_max*nums[i],cur_min*nums[i])
10            cur_min=min(nums[i],cur_min*nums[i],temp_max*nums[i])
11        
12            res=max(cur_max, res)
13        return res