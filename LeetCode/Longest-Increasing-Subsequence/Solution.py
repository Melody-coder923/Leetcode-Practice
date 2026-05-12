1class Solution:
2    def lengthOfLIS(self, nums: List[int]) -> int:
3        n=len(nums)
4        res=[]
5        for num in nums:
6            l,r=0,len(res)-1
7            while l<=r:
8                mid=(r+l)//2
9                if res[mid]<num:
10                    l=mid+1
11                else:
12                    r=mid-1
13            if l==len(res):
14                res.append(num)
15            else:
16                res[l]=num
17        return len(res)