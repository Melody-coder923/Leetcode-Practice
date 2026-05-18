1class Solution:
2    def minRemoval(self, nums: List[int], k: int) -> int:
3        nums.sort()
4        n=len(nums)
5        l=0
6        best=0
7        for r in range(n):
8            while nums[r] > nums[l] * k: #不符合要求
9                l+=1
10            best=max(best,r-l+1) #符合要求的长度越长越好
11        
12        return n-best
13