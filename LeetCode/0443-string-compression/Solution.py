class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        l, r = 0, 0

        while r < n:
            prev = chars[r]
            count = 0

            # 统计当前字符出现的次数
            while r < n and chars[r] == prev:
                count += 1
                r += 1

            # 写入当前字符
            chars[l] = prev
            l += 1

            # 写入字符出现的次数
            if count > 1:
                for digit in str(count):
                    chars[l] = digit
                    l += 1

        return l