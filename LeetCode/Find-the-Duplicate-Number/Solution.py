1#当作链表"
2class Solution:
3    def findDuplicate(self, nums: List[int]) -> int:
4        fast=slow=nums[0]
5        while True:
6            slow=nums[slow]
7            fast=nums[nums[fast]]
8            if slow==fast:
9                break
10        slow=nums[0]
11        while slow!=fast:
12            slow=nums[slow]
13            fast=nums[fast]
14        return slow
15