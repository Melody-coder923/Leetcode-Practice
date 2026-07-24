1class Solution:
2    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
3        left,right=0,0
4        prod=1
5        res=0
6        while right<len(nums):  # right: 
7            prod*=nums[right]  #
8            right+=1
9            while left<right and prod>=k:  #k=100  滑动窗口
10                prod//=nums[left] 
11                left+=1  #left: 
12            res+=right-left
13        return res
14
15