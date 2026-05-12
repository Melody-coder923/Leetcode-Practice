1class Solution:
2    def lengthOfLIS(self, nums: List[int]) -> int:
3        d=[]
4        for x in nums:  
5            i = bisect_left(d, x) 
6            if i == len(d): 
7                d.append(x) 
8            else:  
9                d[i] = x 
10        return len(d)  