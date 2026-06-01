1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        from collections import defaultdict
4        left=0
5        maxcount=0
6        maxlength=0
7        count=defaultdict(int)
8        for right in range(len(s)):
9                count[s[right]]+=1
10                maxcount=max(maxcount, count[s[right]])
11                while (right-left+1)-maxcount>k:
12                    count[s[left]]-=1
13                    left+=1
14                maxlength=max(right-left+1,maxlength)
15        return maxlength