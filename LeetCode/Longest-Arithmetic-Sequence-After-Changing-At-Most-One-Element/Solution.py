1class Solution:
2    def longestArithmetic(self, nums: List[int]) -> int:
3        n = len(nums)
4        if n <= 2:
5            return n
6
7        # left[i] = 以 i 结尾的最长等差连续子数组长度
8        left = [2] * n
9        left[0] = 1
10        for i in range(2, n):
11            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
12                left[i] = left[i - 1] + 1
13
14        # right[i] = 以 i 开头的最长等差连续子数组长度
15        right = [2] * n
16        right[n - 1] = 1
17        for i in range(n - 3, -1, -1):
18            if nums[i + 1] - nums[i] == nums[i + 2] - nums[i + 1]:
19                right[i] = right[i + 1] + 1
20
21        ans = 2
22
23        # 修改最左端 or 最右端
24        ans = max(ans, right[1] + 1)
25        ans = max(ans, left[n - 2] + 1)
26
27        # 枚举修改中间位置 i
28        for i in range(1, n - 1):
29            l, r = i - 1, i + 1
30
31            # 只接左边 or 只接右边
32            ans = max(ans, left[l] + 1)
33            ans = max(ans, right[r] + 1)
34
35            # 尝试把左右整段接起来
36            s = nums[l] + nums[r]
37            if s % 2 != 0:
38                continue
39
40            new_val = s // 2
41            diff = new_val - nums[l]
42
43            cur = 3  # nums[l], 改后的 nums[i], nums[r]
44
45            # 左边这整段能不能和中间统一公差
46            if l > 0 and nums[l] - nums[l - 1] == diff:
47                cur += left[l] - 1
48
49            # 右边这整段能不能和中间统一公差
50            if r < n - 1 and nums[r + 1] - nums[r] == diff:
51                cur += right[r] - 1
52
53            ans = max(ans, cur)
54
55        return ans