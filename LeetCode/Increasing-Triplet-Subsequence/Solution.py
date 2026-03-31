1class Solution:
2    def increasingTriplet(self, nums: List[int]) -> bool:
3        v1=v2=float("inf")
4        #v1<v2<num
5        for num in nums:
6            if num<v1:
7                v1=num
8            if num>v1 and num<v2:
9                v2=num
10            if num>v1 and num>v2:
11                return True
12        return False
13            