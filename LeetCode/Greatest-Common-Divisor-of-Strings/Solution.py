1class Solution:
2    def gcdOfStrings(self, str1: str, str2: str) -> str:
3        if str1+str2!=str2+str1:
4            return ""
5        k = math.gcd(len(str1), len(str2))
6        return str1[:k]