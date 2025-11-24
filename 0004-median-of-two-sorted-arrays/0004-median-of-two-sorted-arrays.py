class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Step 0: 让 nums1 是较短的数组
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        # 特殊情况：两个数组都为空
        if m == 0 and n == 0:
            return 0.0

        # Step 1: 二分查找切割点 i
        # i 本质上是“左边有几个元素”,不是一个数组索引
        l, r = 0, m
        while l <= r:
            i = (l + r) // 2               # nums1 左边元素数量
            j = (m + n + 1) // 2 - i       # nums2 左边元素数量

            # Step 1a: 处理边界情况
            maxleft1  = float("-inf") if i == 0 else nums1[i-1]
            minright1 = float("inf")  if i == m else nums1[i]
            maxleft2  = float("-inf") if j == 0 else nums2[j-1]
            minright2 = float("inf")  if j == n else nums2[j]

            # Step 1b: 判断是否找到正确的切割
            if maxleft1 <= minright2 and maxleft2 <= minright1:
                # Step 2: 根据总长度奇偶数返回中位数
                if (m + n) % 2 == 1:
                    # 奇数：取左边最大值
                    return max(maxleft1, maxleft2)
                else:
                    # 偶数：取左边最大值和右边最小值的平均
                    return (max(maxleft1, maxleft2) + min(minright1, minright2)) / 2

            # Step 1c: 移动切割点
            elif maxleft1 > minright2:
                # nums1 左边太大，i 需要左移
                r = i - 1
            else:
                # nums1 左边太小，i 需要右移
                l = i + 1

        # 理论上不会走到这里
        return 0.0
