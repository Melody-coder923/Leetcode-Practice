1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        if x < 0 or (x % 10 == 0 and x != 0):
4            return False
5
6        reverted = 0
7
8        # x=12 3 21
9        # 反转数字后半部分
10        while x > reverted: #x=12
11            reverted = reverted * 10 + x % 10  # reverted=123
12            x //= 10
13
14        # 判断前半部分和反转后的后半部分是否相等（考虑奇数长度情况） 
15        return x == reverted or x == reverted // 10 