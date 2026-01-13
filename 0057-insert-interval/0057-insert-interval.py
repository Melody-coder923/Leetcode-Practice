class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 基准是 newInterval
        # 被判断的对象是intervals
        res = []
        new_start, new_end = newInterval
        inserted = False
        
        for start, end in intervals:
            # 左边
            if end < new_start:
                res.append([start, end])
            # 右边
            elif start > new_end:
                if not inserted:
                    res.append([new_start, new_end])
                    inserted = True
                res.append([start, end])
            # 重叠
            else:
                new_start = min(new_start, start)
                new_end = max(new_end, end)

        if not inserted:
            res.append([new_start, new_end])

        return res