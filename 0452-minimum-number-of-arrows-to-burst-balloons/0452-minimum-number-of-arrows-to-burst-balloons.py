class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Input: xstart xend points
        # 目标 → 最少点覆盖所有区间 ->x_end in order
        points.sort(key=lambda x: x[1])
        arrows = 0
        current_arrow = float('-inf')  # 当前箭射点初始化为负无穷
        for interval in points:
            if interval[0] > current_arrow:
                # 当前区间左端点在箭射点右边，需要新箭
                arrows += 1
                current_arrow = interval[1]  # 射在当前区间右端点
        return arrows