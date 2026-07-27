1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        count=1
4        res=nums[0]
5
6        for num in nums[1:]:
7            if count==0:
8                res=num
9
10            if num==res:
11                count+=1
12            else:
13                count-=1
14
15        return res