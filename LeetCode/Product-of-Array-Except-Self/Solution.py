1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        n=len(nums)
4        ans=[1]*n
5        left=1
6        for i in range(n):
7            ans[i]=left
8            left*=nums[i]
9        right=1
10        for j in range(n-1,-1,-1):
11            ans[j]*=right
12            right*=nums[j]
13        return ans