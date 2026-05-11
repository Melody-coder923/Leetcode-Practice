1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        cur_max=nums[0]
4        cur_min=nums[0]
5        res=nums[0]
6
7        for i in range(1,len(nums)):
8            temp=cur_max
9            cur_max=max(cur_max*nums[i], cur_min*nums[i], nums[i])
10            cur_min=min(temp * nums[i], cur_min*nums[i], nums[i])
11            res=max(cur_max,res)
12        return res