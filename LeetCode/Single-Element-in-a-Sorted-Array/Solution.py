1"""
2因为元素成对出现，单独元素会打破“第一个出现的元素在偶数位置，第二个在奇数位置”的规律。
3对 mid 做调整为偶数索引，判断 nums[mid] 和 nums[mid+1] 是否相等，缩小搜索区间。
4"""
5class Solution:
6    def singleNonDuplicate(self, nums: List[int]) -> int:
7        l,r=0,len(nums)-1
8        while l<r:
9            mid=(l+r)//2
10            if mid%2==1:
11                mid-=1
12            if nums[mid]==nums[mid+1]:
13                l=mid+2
14            
15            else: #当前配对被打破，单独元素在 mid 或左边
16                r=mid
17        
18        return nums[l]