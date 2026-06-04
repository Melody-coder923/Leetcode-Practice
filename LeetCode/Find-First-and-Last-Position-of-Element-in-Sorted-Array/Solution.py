1class Solution:
2    def searchRange(self, nums: List[int], target: int) -> List[int]:
3        if not nums:
4            return [-1,-1]
5        def get_left(l,r):
6            while l<=r:
7                mid=(l+r)//2
8                if nums[mid]<target:
9                    l=mid+1
10                else:
11                    r=mid-1
12            return l
13
14        def get_right(l,r):
15            while l<=r:
16                mid=(l+r)//2
17                if nums[mid]<=target:
18                    l=mid+1
19                else:
20                    r=mid-1
21            return r
22        n=len(nums)
23        left=get_left(0,n-1)
24        right=get_right(0,n-1)
25        if left >= n or nums[left] != target:
26            return [-1,-1]
27        return [left, right]