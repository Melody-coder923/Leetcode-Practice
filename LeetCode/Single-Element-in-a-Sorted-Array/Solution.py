1"""
2因为元素成对出现，单独元素会打破“第一个出现的元素在偶数位置，第二个在奇数位置”的规律。
3对 mid 做调整为偶数索引，判断 nums[mid] 和 nums[mid+1] 是否相等，缩小搜索区间。
4"""
5class Solution:
6    def singleNonDuplicate(self, nums: List[int]) -> int:
7        left = 0
8        right = len(nums) - 1
9
10        while left < right:
11            mid = left + (right - left) // 2
12
13            # 保证 mid 是偶数下标
14            if mid % 2 == 1:
15                mid -= 1
16
17            if nums[mid] == nums[mid + 1]:
18                # 当前这一对正常，单独元素在右边
19                left = mid + 2
20            else:
21                # 当前配对被打破，单独元素在 mid 或左边
22                right = mid
23
24        return nums[left]