class Solution:
    def romanToInt(self, s: str) -> int:
        # Step1: build dict
        map= { "I": 1, "V":5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        if len(s)==1:
            return map[s[0]]
        #  For loop reverse
        res=0
        for i in range(len(s)-1,-1,-1):
            if i < len(s) - 1 and map[s[i]] < map[s[i + 1]]:
                res-=map[s[i]]
            else:
                res+=map[s[i]]
        return res