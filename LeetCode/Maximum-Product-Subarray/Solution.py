1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        n=len(nums)
4        dp_max=[0]*n
5        dp_min=[0]*n
6        
7        dp_max[0]=nums[0]
8        dp_min[0]=nums[0]
9        res=nums[0]
10
11        for i in range(1,n):
12            dp_max[i]=max(nums[i], dp_max[i-1]*nums[i], dp_min[i-1]*nums[i])
13            dp_min[i]=min(nums[i], dp_max[i-1]*nums[i], dp_min[i-1]*nums[i])
14            res=max(dp_max[i],res)
15        
16        return res 