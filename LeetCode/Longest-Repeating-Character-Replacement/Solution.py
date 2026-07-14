1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        l=0
4        n=len(s)
5        res=0
6        maxletter=0
7        window=defaultdict(int)
8        for r in range(n):
9            window[s[r]]+=1
10            maxletter = max(maxletter, window[s[r]])
11            while (r - l + 1) - maxletter > k:
12                window[s[l]] -= 1
13                l += 1
14
15            res = max(res, r - l + 1)
16        return res
17    