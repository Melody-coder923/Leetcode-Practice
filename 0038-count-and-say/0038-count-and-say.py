class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev = self.countAndSay(n - 1)
        res = []
        
        i = 0
        while i < len(prev):
            digit = prev[i]
            count = 1
            # 统计连续相同的数字
            while i + 1 < len(prev) and prev[i + 1] == digit:
                count += 1
                i += 1
            res.append(str(count) + digit)
            i += 1
        
        return ''.join(res)