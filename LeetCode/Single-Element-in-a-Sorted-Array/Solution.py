1class Solution:
2    def singleNonDuplicate(self, nums: List[int]) -> int:
3        l,r=0,len(nums)-1
4        while l<r:
5            mid=(l+r)//2
6            if mid%2==1:
7                mid-=1
8            if nums[mid]!=nums[mid+1]:
9                r=mid
10            else:
11                l=mid+2
12        
13        return nums[l]
14    
15  