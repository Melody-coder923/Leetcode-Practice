1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        farest=0
4        for i,num in enumerate(nums):
5            if i>farest:
6                return False
7            if farest>=len(nums)-1:
8                return True
9            farest=max(farest,nums[i]+i)
10        return True