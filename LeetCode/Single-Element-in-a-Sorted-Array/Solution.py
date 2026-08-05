1class Solution:
2    def singleNonDuplicate(self, nums: List[int]) -> int:
3        if len(nums)==1:
4            return nums[0]
5
6        l,r=0,len(nums)-1
7        while l<r:
8            mid=(l+r)//2
9            if mid%2==1:
10                mid-=1
11            if nums[mid]!=nums[mid+1]:
12                r=mid
13            else:
14                l=mid+2
15        
16        return nums[l]
17