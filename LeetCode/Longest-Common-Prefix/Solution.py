1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        if not strs:
4            return ""
5
6        if len(strs)<=1:
7            return strs[0]
8        
9        for i in range(len(strs[0])): #0,1,2
10            char=strs[0][i] # f l o w e r
11            for word in strs[1:]: # flow, flight
12                if i==len(word) or char!=word[i]:
13                    return strs[0][:i]
14        return strs[0]