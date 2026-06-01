1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        maxcur=mincur=res=nums[0]
4
5        for num in nums[1:]:
6            temp=maxcur
7            maxcur=max(num,maxcur*num,mincur*num)
8            mincur=min(num,temp*num,mincur*num)
9
10            res=max(res,maxcur)
11        return res