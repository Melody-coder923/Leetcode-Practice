1class Solution:
2    def maxCoins(self, nums: List[int]) -> int:
3        nums=[1]+nums+[1]
4        n=len(nums)
5        
6        @lru_cache(None)
7        def dfs(l,r):
8            if r-l==1:
9                return 0
10            #l 1 r
11            res=0
12            for i in range(l+1,r):
13                res=max(dfs(l,i)+nums[l]*nums[r]*nums[i]+dfs(i,r),res)
14            
15            return res
16
17        return dfs(0,n-1)
18
19        """
20
21        [l    i     r]
22         1          1
23        """