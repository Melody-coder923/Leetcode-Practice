1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        n=len(nums)
4        curMax=nums[0]
5        curMin=nums[0]
6        res=nums[0]
7
8        for i in range(1, n):
9            temp= curMax
10            curMax=max(nums[i],nums[i]*curMax,nums[i]*curMin)
11            curMin=min(nums[i],nums[i]*temp,nums[i]*curMin)
12            res=max(res,curMax)
13        
14        return res
15
16