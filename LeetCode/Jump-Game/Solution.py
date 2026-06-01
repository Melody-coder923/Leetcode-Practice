1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        farest=0
4        for i,num in enumerate(nums):
5            if farest<i:
6                return False
7            if i+num>=len(nums)-1:
8                return True
9            farest=max(farest,i+num)
10            
11        
12