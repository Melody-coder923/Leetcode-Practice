1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        l, r = 0, len(nums) - 1
4        while l < r:
5            mid = l + (r - l) // 2
6            if nums[mid] > nums[r]:
7                l = mid + 1
8            else:
9                r = mid  
10        return nums[l]