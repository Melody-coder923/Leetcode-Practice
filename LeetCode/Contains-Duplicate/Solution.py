1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        a=len(nums)
4        b=len(set(nums))
5        if a>b: 
6            return True
7        else:
8            return False