class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # edge case
        if not strs:
            return ""
        n=len(strs)
        if n==1:
            return strs[0]
        # suppose the first one is prefix to short it
        for i in range(len(strs[0])):
            c = strs[0][i]
            for s in strs:
                if i == len(s) or s[i] != c:
                    return strs[0][:i]
        return strs[0]
"""
    def longestCommonPrefix(s):
        if not s:
            return ""
        prefix = s[0]
        for word in s[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix    
"""