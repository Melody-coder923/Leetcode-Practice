1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        max_reach = 0 
4        for i,num in enumerate(nums):
5            if i>max_reach:
6                return False
7            max_reach = max(max_reach, i + nums[i])
8            if max_reach >= len(nums) - 1:
9                return True
10        return True