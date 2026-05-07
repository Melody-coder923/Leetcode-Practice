1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        curr_max=nums[0]
4        curr_min=nums[0]
5
6        res=nums[0]
7        for num in nums[1:]:
8
9            temp_max = curr_max
10
11            curr_max = max(
12                num,
13                curr_max * num,
14                curr_min * num
15            )
16
17            curr_min = min(
18                num,
19                temp_max * num,
20                curr_min * num
21            )
22            res = max(res, curr_max)
23
24        return res