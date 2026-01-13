class Solution:
    def maxScore(self, s: str) -> int:
        """
            1. 求什么? 得分 = 左 0 + 右 1 ,想要最大值, 自然想到：左边多 0、右边多 1 → 好的切分点
            2. 能不能量化? 左边 0 的数量 → 从左往右累计, 右边 1 的数量 → 从右往左累计.这里就是前缀 / 后缀计数的萌芽
            3. 左边 0 的数量 → 前缀数组 left_zeros[i] ,右边 1 的数量 → 后缀数组 right_ones[i]
            4. score[i] = left_zeros[i] + right_ones[i+1]
            5. 考虑效率优化: 从左往右扫，左边 0 +1，右边 1 总数减去遇到的 1 → O(1) 空间
            6. score[i] = 左边0个数 + 右边1个数 -> 右边 1 的个数 = 总 1 的数量 - 左边已经遇到的 1 个数
        """

        #先统计整个数组中 1 的总数
        total_ones = s.count('1')
        left_zeros = 0 #left_zeros：左边遇到的 0 的数量
        left_ones = 0 #左边遇到的 1 的数量
        max_score = 0
        #遍历只考虑切点 0 .. n-2（长度 n=2，只能切 i=0）
        for i in range(len(s)-1):
            if s[i] == '0':
                left_zeros += 1
            else:
                left_ones += 1
            score = left_zeros + (total_ones - left_ones)
            max_score = max(max_score, score)

        return max_score