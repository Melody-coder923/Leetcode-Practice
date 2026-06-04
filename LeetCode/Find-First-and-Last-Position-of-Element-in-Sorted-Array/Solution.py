1class Solution:
2    def searchRange(self, nums: List[int], target: int) -> List[int]:
3        def getLeft():
4            left, right = 0, len(nums) - 1
5            while left <= right:
6                mid = (left + right) // 2  # 保留 mid
7                # if nums[mid] == target: pass  # 可选练习用注释
8                if nums[mid] < target:
9                    left = mid + 1
10                else:
11                    right = mid - 1
12            return left
13
14        def getRight():
15            left, right = 0, len(nums) - 1
16            while left <= right:
17                mid = (left + right) // 2  # 保留 mid
18                # if nums[mid] == target: pass  # 可选练习用注释
19                if nums[mid] <= target:
20                    left = mid + 1
21                else:
22                    right = mid - 1
23            return right
24
25        left_idx = getLeft()
26        right_idx = getRight()
27
28        if left_idx <= right_idx:
29            return [left_idx, right_idx]
30        else:
31            return [-1, -1]