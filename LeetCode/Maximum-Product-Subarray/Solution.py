1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        n=len(nums)
4        dp_max = [0] * n
5        dp_min = [0] * n
6
7        dp_max[0] = nums[0]
8        dp_min[0] = nums[0]
9        res=nums[0]
10        for i in range(1,n):
11            dp_max[i] = max(
12                nums[i],
13                dp_max[i-1] * nums[i],
14                dp_min[i-1] * nums[i]
15            )
16
17            dp_min[i] = min(
18                nums[i],
19                dp_max[i-1] * nums[i],
20                dp_min[i-1] * nums[i]
21            )
22            res = max(res, dp_max[i])
23
24        return res
25