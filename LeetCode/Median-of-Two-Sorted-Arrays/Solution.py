1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        # Step 0: 让 nums1 是较短的数组
4        m, n = len(nums1), len(nums2)
5        if m > n:
6            nums1, nums2 = nums2, nums1
7            m, n = n, m
8
9        # 特殊情况：两个数组都为空
10        if m == 0 and n == 0:
11            return 0.0
12
13        # Step 1: 二分查找切割点 i
14        # i 本质上是“左边有几个元素”,不是一个数组索引
15        l, r = 0, m
16        while l <= r:
17            i = (l + r) // 2               # nums1 左边元素数量
18            j = (m + n + 1) // 2 - i       # nums2 左边元素数量
19
20            # Step 1a: 处理边界情况
21            maxleft1  = float("-inf") if i == 0 else nums1[i-1]
22            minright1 = float("inf")  if i == m else nums1[i]
23            maxleft2  = float("-inf") if j == 0 else nums2[j-1]
24            minright2 = float("inf")  if j == n else nums2[j]
25
26            # Step 1b: 判断是否找到正确的切割
27            if maxleft1 <= minright2 and maxleft2 <= minright1:
28                # Step 2: 根据总长度奇偶数返回中位数
29                if (m + n) % 2 == 1:
30                    # 奇数：取左边最大值
31                    return max(maxleft1, maxleft2)
32                else:
33                    # 偶数：取左边最大值和右边最小值的平均
34                    return (max(maxleft1, maxleft2) + min(minright1, minright2)) / 2
35
36            # Step 1c: 移动切割点
37            elif maxleft1 > minright2:
38                # nums1 左边太大，i 需要左移
39                r = i - 1
40            else:
41                # nums1 左边太小，i 需要右移
42                l = i + 1
43
44        # 理论上不会走到这里
45        return 0.0
46