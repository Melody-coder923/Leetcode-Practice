class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        #差分数组
        diff = [0] * (n + 1)
        # 差分标记每盏灯照亮的区间,每盏灯照亮一段区间
        for pos, r in lights:
            #防止照亮范围超出左边界
            left = max(0, pos - r)
            #防止照亮范围超出右边界
            right = min(n - 1, pos + r)
            diff[left] += 1
            if right + 1 < n:
                #防止数组越界，因为 diff[right+1] 可能超出范围
                diff[right + 1] -= 1
        # 通过前缀和恢复亮度 [1:3]
        #diff = [0, 1, 0, 0, -1]
        #presum
        #brightness = [0, 1, 1, 1, 0]
        brightness = [0] * n
        brightness[0] = diff[0]
        for i in range(1, n):
            brightness[i] = brightness[i - 1] + diff[i]

        # 统计满足条件的点
        ans = sum(brightness[i] >= requirement[i] for i in range(n))
        return ans