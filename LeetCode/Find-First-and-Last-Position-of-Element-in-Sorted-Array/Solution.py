1class Solution:
2    def searchRange(self, nums: List[int], target: int) -> List[int]:
3        if not nums:
4            return [-1, -1]
5        l,r=0,len(nums)-1
6        res=[]
7        while l<r:
8            mid= l+(r-l)//2
9            if nums[mid]<target:
10                l=mid+1
11            else:
12                r=mid
13        
14        if nums[l] != target:
15            return [-1, -1]
16        
17        left = l
18
19        l, r = 0, len(nums) - 1
20        while l<r:
21            mid = l + (r - l + 1) // 2
22            if nums[mid]<=target:
23                l = mid
24            else:
25                r = mid-1
26        right = l
27        return [left, right]
28