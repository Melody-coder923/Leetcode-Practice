1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        from collections import defaultdict
4        start=0
5        maxcount=0
6        maxlength=0
7        count=defaultdict(int)
8        for end in range(len(s)):
9            count[s[end]]+=1
10            maxcount = max(maxcount, count[s[end]])
11
12            while (end - start + 1) - maxcount > k:
13                count[s[start]] -= 1 
14                start+=1
15            maxlength = max(maxlength, end - start + 1)
16        
17        return maxlength