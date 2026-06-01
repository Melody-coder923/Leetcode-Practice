1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        #sliding window最后可以有k个不一样的，否则挪动l
4        # 不一样的= sliding window长度 - 最多的一样的字母数量
5        l = 0
6        count = defaultdict(int)
7        maxletter = 0
8        res = 0
9
10        for r in range(len(s)):
11            count[s[r]] += 1
12            maxletter = max(maxletter, count[s[r]])
13
14            while (r - l + 1) - maxletter > k:
15                count[s[l]] -= 1
16                l += 1
17
18            res = max(res, r - l + 1)
19
20        return res
21
22