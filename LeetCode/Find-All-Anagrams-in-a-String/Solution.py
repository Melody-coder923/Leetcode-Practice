1class Solution:
2    def findAnagrams(self, s: str, p: str) -> List[int]:
3        if len(s) < len(p):
4            return []
5
6        target = [0] * 26
7        window = [0] * 26
8
9        for c in p:
10            target[ord(c) - ord('a')] += 1
11
12        res = []
13        k = len(p)
14
15        for r in range(len(s)):
16            window[ord(s[r]) - ord('a')] += 1
17
18            # 窗口超过 p 长度，移除左边
19            if r >= k:
20                window[ord(s[r - k]) - ord('a')] -= 1
21
22            # 窗口长度达到 k
23            if r >= k - 1 and window == target:
24                res.append(r - k + 1)
25
26        return res