class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict=defaultdict(int)
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in dict and dict[s[r]]>=l:
                    l=dict[s[r]]+1
            
            dict[s[r]]=r
            res=max(res,r-l+1)

        return res
