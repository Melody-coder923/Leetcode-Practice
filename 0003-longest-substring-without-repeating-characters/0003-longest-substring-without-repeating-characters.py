class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        
        dic = {}
        left = 0
        maxlength = 0
        
        for right, char in enumerate(s):
            if char in dic and dic[char] >= left:
                left = dic[char] + 1
            dic[char] = right
            maxlength = max(maxlength, right - left + 1)
        
        return maxlength
                



        
        