1class Solution:
2    def lengthOfLIS(self, nums: List[int]) -> int:
3        d = []  # 用来维护一个递增序列
4        for x in nums:  # 遍历 nums 里的每个数
5            i = bisect_left(d, x)  # 在 d 中找第一个 >= x 的位置索引
6            if i == len(d):  # 如果没找到（x 比所有数都大）
7                d.append(x)  # 直接加到末尾
8            else:  # 否则
9                d[i] = x  # 替换这个位置的数为 x
10        return len(d)  # d 的长度就是 LIS 长度