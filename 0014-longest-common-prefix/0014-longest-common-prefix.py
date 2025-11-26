class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        if not strs:
            return ""
        strs.sort(key=len)
        prefix = strs[0] 
        for item in strs[1:]:
            while not item.startswith(prefix):
                prefix=prefix[:-1]
                if prefix=="":
                    return ""   
        return prefix