1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        if not strs:
4            return ""
5        if len(strs)==1:
6            return strs[0]
7        
8        for i in range(len(strs[0])):
9            char=strs[0][i]
10            for word in strs[1:]:
11                if i==len(word) or char!=word[i]:
12                    return strs[0][:i]
13        
14        return strs[0]
15                