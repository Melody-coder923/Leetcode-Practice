class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map={}
        l=0
        res=0
        for r,char in enumerate(s):
            if char in map and map[char]>=l:
                l=map[char]+1
            res=max(res,r-l+1)
            map[char]=r
        return res
