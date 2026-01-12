class Solution:
    def bestClosingTime(self, customers: str) -> int:
        #它用的是「前缀/差分思想 + 代价累计」
        """
        商店在某个时间点 i 关门
        i 之前：
        来顾客（Y）是好事
        不来顾客（N）是坏事（罚分）
        i 之后：
        来顾客（Y）是坏事（关门了还来）
        不来顾客（N）是好事
        👉 每个时间点的状态，对“关门时间 i”都有正负贡献
        对区间做 +1 / -1
        """
        #不要每次重算罚分，而是“关门时间往右挪一步，只更新这一位带来的变化”
        # 初始情况：i = 0，全部时间都关门
        penalty = customers.count('Y')
        
        min_penalty = penalty
        best_time = 0
        
        # i 从 1 到 n
        for i, c in enumerate(customers):
            if c == 'Y':
                penalty -= 1   # Y 从“关门后”变成“开门前”
            else:  # c == 'N'
                penalty += 1   # N 从“关门后”变成“开门前”
            
            if penalty < min_penalty:
                min_penalty = penalty
                best_time = i + 1
        
        return best_time
        """
            for i in range(n + 1):
            算左边罚分
            算右边罚分
        """