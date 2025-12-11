class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        if len(strs)<=1:
            return strs[0]
        
        for i in range(len(strs[0])):
            c=strs[0][i]
            for char in strs[1:]:
                if i==len(char) or c!=char[i]:
                    return char[:i]

        return strs[0]