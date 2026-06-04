1class Solution:
2    def searchRange(self, nums: List[int], target: int) -> List[int]:
3        if not nums:
4            return [-1, -1]
5        def findleft(l,r):
6            while l<=r:
7                mid=(l+r)//2
8                if nums[mid]<target:
9                    l=mid+1
10                else:
11                    r=mid-1
12            return l
13
14        def findright(l,r):
15            while l<=r:
16                mid=(l+r)//2
17                if nums[mid]<=target:
18                    l=mid+1
19                else:
20                    r=mid-1
21            return r
22            
23        n=len(nums)
24        Left =findleft(0,n-1)
25        Right =findright(0,n-1)
26        if Left <= Right and nums[Left] == target:
27            return [Left, Right]
28        else:
29            return [-1,-1]