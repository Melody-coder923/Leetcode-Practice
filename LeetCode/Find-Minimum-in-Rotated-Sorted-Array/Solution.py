1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        n=len(nums)
4        if n==1:
5            return nums[0]
6        
7        l,r=0,n-1
8        while l<r:
9            mid= l+(r-l)//2
10            if nums[mid]>nums[r]:
11                l=mid+1
12            else:
13                r=mid  # 不排除mid 
14
15        return nums[l]