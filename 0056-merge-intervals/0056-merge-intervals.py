class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]  # 第一个区间直接加入

        for cur in intervals[1:]:
            last = res[-1]
            if cur[0] <= last[1]:  # 有重叠
                last[1] = max(last[1], cur[1])  # 合并
            else:
                res.append(cur)  # 无重叠，直接加入

        return res