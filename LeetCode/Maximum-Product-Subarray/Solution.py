1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        n=len(nums)
4        curr_max=nums[0]
5        curr_min=nums[0]
6        res=nums[0]
7
8        for i in range(1,n):
9            temp_max=curr_max
10            curr_max=max(nums[i],curr_max*nums[i],curr_min*nums[i])
11            curr_min=min(nums[i],curr_min*nums[i],temp_max*nums[i])
12            res=max(curr_max,res)
13        return res