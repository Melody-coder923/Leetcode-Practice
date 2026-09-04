1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        n=len(nums)
4        if n<=2:
5            return n
6        slow=2
7        for fast in range(2,n):
8            if nums[fast]!=nums[slow-2]:
9                nums[slow]=nums[fast]
10                slow+=1
11        
12        return slow