class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """
         翻转次数 = “把一些 0 → 1” + “把一些 1 → 0”
         目标是让所有 0 在左，1 在右
         如果我们选择一个切分点 i： 左边 [0..i] → 全部改成 0 ,  右边 [i+1..n-1] → 全部改成 1 ,
         对每个切分点，计算需要翻转的次数 → 最小值就是答案
         这就是最直观的“左右贡献 + 前缀和”思路
        
            左边0=count_zero_left
            左边需要翻转次数 = i+1 - count_zeros_in_left → 翻成 0 的次数 = 左边 1 的数量

            右边 1 的数量 = count_ones_in_right
            右边需要翻转次数 = (n-i-1) - count_ones_in_right → 翻成 1 的次数 = 右边 0 的数量

            total_flip = (左边 1 的数量) + (右边 0 的数量)
            左边 1 的数量 → 用前缀和可以 O(1) 得到
            右边 0 的数量 → 总 0 数 - 左边 0 数 → O(1)
        """
        ones = 0          # 左边 1 的数量
        min_flip = 0
        for c in s:
            if c == '1':
                ones += 1
            else:  # c == '0'
                # flip = 左边1 + 当前0翻成1 把这个0翻掉, 把左边所有1翻掉
                min_flip = min(min_flip + 1, ones)
        return min_flip



        """
                翻成0 (左边是1)   |  翻成1(右边是0)
                total=左边1+右边0
                    1用前缀和  + (总0数量-左边0数量)
        """