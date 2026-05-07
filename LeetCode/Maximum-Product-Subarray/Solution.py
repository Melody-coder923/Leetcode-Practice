1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        left = 1
4        right = 1
5        n = len(nums)
6        res = max(nums)
7
8        for i in range(n):
9            left *= nums[i]
10            right *= nums[n - 1 - i]
11
12            res = max(res, left, right)
13
14            if left == 0:
15                left = 1
16            if right == 0:
17                right = 1
18
19        return res
20