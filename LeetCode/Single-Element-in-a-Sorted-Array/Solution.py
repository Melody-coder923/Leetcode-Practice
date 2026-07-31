1"""
2因为元素成对出现，单独元素会打破“第一个出现的元素在偶数位置，第二个在奇数位置”的规律。
3对 mid 做调整为偶数索引，判断 nums[mid] 和 nums[mid+1] 是否相等，缩小搜索区间。
4"""
5class Solution:
6    def singleNonDuplicate(self, nums: List[int]) -> int:
7        res=nums[0]
8        for num in nums[1:]:
9            res^=num
10        return res