1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:
3        n=len(nums)
4        res=[]
5        nums.sort()
6        for i in range(n-2):
7            if nums[i]>0:
8                break
9            if i>0 and nums[i]==nums[i-1]:
10                continue
11            l,r=i+1,n-1
12            while l<r:
13                total=nums[i]+nums[l]+nums[r]
14                if total==0:
15                    res.append([nums[i],nums[l],nums[r]])
16                    l+=1
17                    r-=1
18                    while l<r and nums[l]==nums[l-1]:
19                        l+=1
20                    while l<r and nums[r]==nums[r+1]:
21                        r-=1
22                    
23                elif total<0:
24                    l+=1
25                else:
26                    r-=1
27        return res