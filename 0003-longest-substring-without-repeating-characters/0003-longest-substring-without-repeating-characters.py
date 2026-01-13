class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        pos = {}
        l = 0
        maxLen = 0

        for r, ch in enumerate(s):
            if ch in pos and pos[ch] >= l:
                l = pos[ch] + 1

            maxLen = max(maxLen, r - l + 1)
            pos[ch] = r

        return maxLen