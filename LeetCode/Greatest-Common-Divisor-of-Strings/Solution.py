1class Solution:
2    def gcdOfStrings(self, str1: str, str2: str) -> str:
3        if str1+str2!=str2+str1:
4            return""
5        def gcd(a,b):
6            while b:
7                a,b=b,a%b
8            return a
9        gcd_length=gcd(len(str1),len(str2))
10        return str1[:gcd_length]