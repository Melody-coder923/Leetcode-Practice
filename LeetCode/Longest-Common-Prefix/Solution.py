1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        # edge case
4        if not strs:
5            return ""
6        n=len(strs)
7        if n==1:
8            return strs[0]
9        # suppose the first one is prefix to short it
10        for i in range(len(strs[0])):
11            c = strs[0][i]
12            for s in strs:
13                if i == len(s) or s[i] != c:
14                    return strs[0][:i]
15        return strs[0]