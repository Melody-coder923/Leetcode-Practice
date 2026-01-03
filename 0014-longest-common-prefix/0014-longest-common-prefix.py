class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        if len(strs)<=1:
            return strs[0]
        
        for i in range(len(strs[0])): #0,1,2
            char=strs[0][i] # f l o w e r
            for word in strs[1:]: # flow, flight
                if i==len(word) or char!=word[i]:
                    return strs[0][:i]
        return strs[0]