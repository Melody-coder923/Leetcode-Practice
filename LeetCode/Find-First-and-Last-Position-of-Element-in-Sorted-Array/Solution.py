1class Solution:
2    def searchRange(self, nums: List[int], target: int) -> List[int]:
3        def getLeft():
4            left, right = 0, len(nums) - 1
5            while left <= right:
6                mid = (left + right) // 2                  
7                if nums[mid] < target:
8                    left = mid + 1
9                else:
10                    right = mid - 1
11            return left
12
13        def getRight():
14            left, right = 0, len(nums) - 1
15            while left <= right:
16                mid = (left + right) // 2 
17                if nums[mid] <= target:
18                    left = mid + 1
19                else:
20                    right = mid - 1
21            return right
22
23        left_idx = getLeft()
24        right_idx = getRight()
25
26        if left_idx <= right_idx:
27            return [left_idx, right_idx]
28        else:
29            return [-1, -1]