1class Solution:
2    def searchRange(self, nums: List[int], target: int) -> List[int]:
3        def findleft(l,r):
4            ans=-1
5            while l<=r:
6                mid=(l+r)//2
7                if nums[mid]>=target:
8                    ans=mid
9                    r=mid-1
10                else:
11                    l=mid+1
12            return ans
13        
14        def findright(l,r):
15            ans=-1
16            while l<=r:
17                mid=(l+r)//2
18                if nums[mid]<=target:
19                    ans=mid
20                    l=mid+1
21                else:
22                    r=mid-1
23            return ans
24
25        n=len(nums)
26        if n == 0:
27            return [-1, -1]
28
29        left = findleft(0, n - 1)
30        if left == -1 or nums[left] != target:
31            return [-1, -1]
32        right = findright(0, n - 1)
33        return [left, right]