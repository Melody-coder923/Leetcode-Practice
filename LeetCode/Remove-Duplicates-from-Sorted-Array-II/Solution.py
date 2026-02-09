1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        slow=2
4        for fast in range(2,len(nums)):
5            if nums[fast]!=nums[slow-2]:
6                nums[slow]=nums[fast]
7                slow+=1
8        return slow
9   