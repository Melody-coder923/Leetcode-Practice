1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(s) != len(t):
4            return False
5        count={}
6        for char in s:
7            if char in count:
8                count[char]+=1
9            else:
10                count[char]=1
11        for char in t:
12            if char in count:
13                count[char]-=1
14            else:
15                return False
16        for value in count.values():
17            if value!= 0:
18                return False
19        return True