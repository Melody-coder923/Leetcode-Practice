1class Solution:
2    def findPeakElement(self, nums: List[int]) -> int:
3        #peak值 可以 是 n-1（最后一个位置）
4        #闭合区间[0,n-2]  因为mid+1不能大于n-1
5        #对应开区间(-1,n-1)
6        #(l, r]   ← 左开右闭 循环结束情况-> 只剩一个 r,r 永远是“可能为峰值”的位置
7        l,r=0, len(nums)-1
8        while l<r:
9            mid= l+(r-l)//2
10            if nums[mid]> nums[mid+1]:
11                r=mid
12            else:
13                l=mid+1
14        return r
15
16     