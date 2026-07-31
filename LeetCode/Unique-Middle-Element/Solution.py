1class Solution:
2    def isMiddleElementUnique(self, nums: list[int]) -> bool:
3        l,r=0,len(nums)-1
4        mid=(l+r)//2
5
6        target= nums[mid]
7        count=0
8        for num in nums:
9            if num==target:
10                count+=1
11        
12        return count==1
13            