class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        def lcm(a, b):
            return a * b // gcd(a, b)
        
        l = lcm(r[0], r[1])
        
        # 二分查找最少时间 T
        left, right = 0, 10**20
        while left < right:
            mid = (left + right) // 2
            
            # 单独计算每台无人机能工作（送货）的时间
            slots1 = mid - (mid // r[0])
            slots2 = mid - (mid // r[1])
            
            # 总共能工作的小时（避免两个同时充电）
            slots_total = mid - (mid // l)
            
            if slots1 >= d[0] and slots2 >= d[1] and slots_total >= (d[0] + d[1]):
                right = mid
            else:
                left = mid + 1
        
        return left