1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        #edge case
4        if not strs:
5            return ""
6        if len(strs)==1:
7            return strs[0]
8        
9        prefix=strs[0]
10        for word in strs[1:]:
11            while not word.startswith(prefix):
12                prefix=prefix[:-1]
13                if not prefix:
14                    return ""
15        
16        return prefix
17                