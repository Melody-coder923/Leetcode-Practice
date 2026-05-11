1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        i,j= 0, len(nums)-1
4        while i<j:
5            mid= i+(j-i)//2
6            if nums[mid]> nums[j]:
7                i=mid+1
8            else:
9                j=mid
10        return nums[i]