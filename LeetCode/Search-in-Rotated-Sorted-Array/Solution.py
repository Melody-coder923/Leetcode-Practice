1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        l,r=0,len(nums)-1
4        while l<=r:
5            mid=l+(r-l)//2
6            if nums[mid]==target:
7                return mid
8            elif nums[mid]<nums[r]:
9                if nums[mid]<target<=nums[r]:
10                    l=mid+1
11                else:
12                    r=mid-1
13            else:
14                if nums[mid]>target>=nums[l]:
15                    r=mid-1
16                else:
17                    l=mid+1
18        return -1                