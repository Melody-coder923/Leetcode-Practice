1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n = len(nums)
4        if n == 1:
5            return nums[0]
6        def helper(arr):
7            n = len(arr)
8
9            if n == 0:
10                return 0
11            if n == 1:
12                return arr[0]
13            if n == 2:
14                return max(arr[0], arr[1])
15
16            prev_nei = arr[0]
17            nei = max(arr[0], arr[1])
18
19            for i in range(2, n):
20                curr = max(prev_nei + arr[i], nei)
21                prev_nei, nei = nei, curr
22
23            return curr
24
25        return max(
26            helper(nums[:-1]),
27            helper(nums[1:])
28        )