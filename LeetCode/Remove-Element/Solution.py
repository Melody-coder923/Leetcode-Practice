1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        fast=slow=0
4        for fast in range(len(nums)):
5            if nums[fast]!=val:
6                nums[slow]=nums[fast]
7                slow+=1
8        return slow