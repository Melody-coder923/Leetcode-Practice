1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        fast=slow=nums[0]
4        while True:
5            fast=nums[nums[fast]]
6            slow=nums[slow]
7            if fast==slow:
8                break
9        
10        slow=nums[0]
11        while fast!=slow:
12            slow=nums[slow]
13            fast=nums[fast]
14        
15        return slow