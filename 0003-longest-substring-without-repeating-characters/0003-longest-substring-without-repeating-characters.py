class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        map=defaultdict(int)
        l=0
        maxLen=0
        for r,char in enumerate(s):
            while char in map and map[char]>=l:
                l=map[char]+1
            maxLen=max(maxLen,r-l+1)
            map[char]=r
        return maxLen