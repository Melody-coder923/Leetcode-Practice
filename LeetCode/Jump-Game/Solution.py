1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        n=len(nums)
4        if n<1:
5            return False
6        farest=0
7        for idx,num in enumerate(nums):
8            if idx > farest:
9                return False
10            farest=max(farest,idx+num)
11            if farest>=n-1:
12                return True
13        return False