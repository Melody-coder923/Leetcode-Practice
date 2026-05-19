1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        n=len(nums)
4        farest=0
5        for i in range(n):
6            if i > farest:
7                return False
8            if nums[i]+i>=n-1:
9                return True
10            farest=max(farest,nums[i]+i)
11        return False
12
13