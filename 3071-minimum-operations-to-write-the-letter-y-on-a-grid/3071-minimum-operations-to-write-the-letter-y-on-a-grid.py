class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        center = n // 2  # 提前计算，避免重复
        
        # 判断是否是Y区域
        def is_Y(r, c):  # 不需要传n，使用外层变量
            if r <= center and r == c:
                return True
            if r <= center and r + c == n - 1:
                return True
            if r >= center and c == center:
                return True
            return False

        # 统计两个区域的颜色分布
        y_count = [0, 0, 0]
        nony_count = [0, 0, 0]
        
        for i in range(n):
            for j in range(n):
                if is_Y(i, j):
                    y_count[grid[i][j]] += 1
                else:
                    nony_count[grid[i][j]] += 1

        # 提前计算总数，避免在循环中重复sum
        y_total = sum(y_count)
        nony_total = sum(nony_count)
        
        # 枚举所有可能的颜色组合并计算最小操作数
        min_ops = float('inf')
        for y_color in range(3):  # 用range(3)更简洁
            for nony_color in range(3):
                if y_color != nony_color:
                    # 直接计算总操作数
                    ops = (y_total - y_count[y_color]) + (nony_total - nony_count[nony_color])
                    min_ops = min(min_ops, ops)
                    
        return min_ops