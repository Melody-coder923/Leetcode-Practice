1class Solution:
2    def pivotIndex(self, nums: List[int]) -> int:
3        # left sum| pivot index |right sum
4        # leftsum 
5        #rightsum=total-leftsum
6
7        leftsum=0
8        total=sum(nums)
9        for idx,num in enumerate(nums):
10            rightsum=total-leftsum-num
11            if leftsum==rightsum:
12                return idx
13            leftsum+=num
14        return -1
15