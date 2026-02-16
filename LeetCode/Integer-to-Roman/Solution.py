1class Solution:
2    def intToRoman(self, num: int) -> str:
3        val_to_roman = [
4            (1000, "M"),
5            (900, "CM"),
6            (500, "D"),
7            (400, "CD"),
8            (100, "C"),
9            (90, "XC"),
10            (50, "L"),
11            (40, "XL"),
12            (10, "X"),
13            (9, "IX"),
14            (5, "V"),
15            (4, "IV"),
16            (1, "I")
17        ]
18        res=""
19        for val, roman in val_to_roman:
20            while num >= val:
21                res += roman
22                num -= val
23        return res