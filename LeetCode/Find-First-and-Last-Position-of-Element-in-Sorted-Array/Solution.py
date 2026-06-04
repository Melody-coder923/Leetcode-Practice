1class Solution:
2    def searchRange(self, nums: List[int], target: int) -> List[int]:
3        def findleft(l,r):
4            while l<=r:
5                mid=(l+r)//2
6                if nums[mid]>=target:
7                    r=mid-1
8                else:
9                    l=mid+1
10            return l
11        
12        def findright(l,r):
13            while l<=r:
14                mid=(l+r)//2
15                if nums[mid]<=target:
16                    l=mid+1
17                else:
18                    r=mid-1
19            return r
20
21        n=len(nums)
22        if n == 0:
23            return [-1, -1]
24
25        left=findleft(0,n-1)
26        right = findright(0, n-1)
27        if left <= right and nums[left] == target:
28            return [left, right]
29        return [-1,-1]