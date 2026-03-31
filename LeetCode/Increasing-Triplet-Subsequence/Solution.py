1class Solution:
2    def increasingTriplet(self, nums: List[int]) -> bool:
3        first,second=float("inf"),float("inf")
4    
5        for n in nums:
6            if n<first:
7                first=n
8            if n>first and n<second:
9                second=n
10            if n>first and n>second:
11                return True
12        return False
13
14            
15            