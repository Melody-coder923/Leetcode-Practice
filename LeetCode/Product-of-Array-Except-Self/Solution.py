1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        result=[]
4        if nums.count(0)>1:
5            return [0]*len(nums)
6        elif nums.count(0)==1:
7            total=1
8            for num in nums:
9                if num !=0:
10                    total*=num
11            return [total if num==0 else 0 for num in nums]
12        else:
13            total = math.prod(nums)
14            return [total//num for num in nums]