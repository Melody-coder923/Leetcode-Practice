1class Solution:
2    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
3        good = [False, False, False]
4        for triplet in triplets:
5            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
6                continue
7            # 这个 triplet 是安全的，看它能贡献 target 的哪一位
8            for i in range(3):
9                if triplet[i] == target[i]:
10                    good[i] = True
11
12        return good[0] and good[1] and good[2]