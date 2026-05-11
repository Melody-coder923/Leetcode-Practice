1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        n=len(nums)
4
5        l,r=0,n-1
6        while l<=r:
7            mid= (r-l)//2+l
8            if nums[mid]== target:
9                return mid
10            elif nums[mid]<nums[r]:
11                if nums[mid]<target<=nums[r]:
12                    l=mid+1
13                else:
14                    r=mid-1
15            else:
16                if nums[l]<=target<nums[mid]:
17                    r=mid-1
18                else:
19                    l=mid+1
20        return -1