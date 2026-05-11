1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        n=len(nums)
4        l,r=0,n-1
5        base=nums[0]
6        big=10**18
7        while l<=r:
8            mid= (r-l)//2+l
9            num=nums[mid]
10            if target < base and nums[mid] >= base:
11                num-=big
12            elif target>=base and nums[mid] <base:
13                num+=big
14            
15            if num<target:
16                l=mid+1
17            elif num>target:
18                r=mid-1
19            else:
20                return mid
21        return -1
22            