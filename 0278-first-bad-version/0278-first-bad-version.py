# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n   # 版本从1开始，r开区间所以+1
    
        while l < r:
            mid = l + (r - l) // 2  # 防溢出
            if isBadVersion(mid):
                r = mid      # 是错误版本，答案在mid或左边
            else:
                l = mid + 1  # 是好版本，答案在右边
        return l