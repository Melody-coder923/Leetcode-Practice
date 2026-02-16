1class Solution:
2    def romanToInt(self, s: str) -> int:
3        # Step1: build dict
4        map= { "I": 1, "V":5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
5        #rules:倒遍历，如果遇到递减，计算减法
6        res=0
7        prev=0
8        for i in range(len(s)-1,-1,-1):
9            if map[s[i]]<prev:
10                res-=map[s[i]]
11            else:
12                res+=map[s[i]]
13            prev=map[s[i]]
14            
15        return res
16       