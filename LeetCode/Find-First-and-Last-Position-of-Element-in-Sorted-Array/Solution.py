1from typing import List
2
3class Solution:
4    def searchRange(self, nums: List[int], target: int) -> List[int]:
5        left = self.find_left(nums, target)
6        right = self.find_right(nums, target)
7        return [left, right]
8
9    def find_left(self, nums: List[int], target: int) -> int:
10        i, j = 0, len(nums)
11        while i < j:
12            mid = i + (j - i) // 2
13            if nums[mid] >= target:
14                j = mid
15            else:
16                i = mid + 1
17        if i < len(nums) and nums[i] == target:
18            return i
19        return -1
20
21    def find_right(self, nums: List[int], target: int) -> int:
22        i, j = 0, len(nums)
23        while i < j:
24            mid = i + (j - i) // 2
25            if nums[mid] > target:
26                j = mid
27            else:
28                i = mid + 1
29        if i > 0 and nums[i - 1] == target:
30            return i - 1
31        return -1