from typing import List

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 10**9 + 7

        inventory.sort(reverse=True)
        inventory.append(0)  # 哨兵

        profit = 0
        n = len(inventory)

        for i in range(n - 1):
            if inventory[i] > inventory[i + 1]:
                # 当前高度差
                diff = inventory[i] - inventory[i + 1]
                # 有多少种颜色在这一层
                cnt = i + 1

                # 这一段最多能卖多少球
                sell = min(orders, diff * cnt)

                full = sell // cnt
                rest = sell % cnt

                # 等差数列求和
                high = inventory[i]
                low = high - full + 1
                profit += cnt * (high + low) * full // 2
                profit += rest * (high - full)

                profit %= MOD
                orders -= sell

                if orders == 0:
                    break

        return profit % MOD
