1# The isBadVersion API is already defined for you.
2# def isBadVersion(version: int) -> bool:
3
4class Solution:
5    def firstBadVersion(self, n: int) -> int:
6        l, r = 1, n   # 版本从1开始，r开区间所以+1
7    
8        while l < r:
9            mid = l + (r - l) // 2  # 防溢出
10            if isBadVersion(mid):
11                r = mid      # 是错误版本，答案在mid或左边
12            else:
13                l = mid + 1  # 是好版本，答案在右边
14        return l