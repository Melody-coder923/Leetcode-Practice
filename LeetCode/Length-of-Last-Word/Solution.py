1class Solution:
2    def lengthOfLastWord(self, s: str) -> int:
3        s = s.strip()
4        words= s.split(" ")
5        last=words[-1]
6        return len(last)