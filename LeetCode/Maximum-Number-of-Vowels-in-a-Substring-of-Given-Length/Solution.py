1class Solution:
2    def maxVowels(self, s: str, k: int) -> int:
3        # set of vowel o(1)
4        vowel={'a', 'e', 'i', 'o', 'u'}
5        # l,r to control window size is k
6        window=s[:k] #abc
7        # count
8        count=0
9
10        for char in window:
11            if char in vowel:
12                count+=1
13        maxcount=count
14        l=0
15        for r in range(k,len(s)):
16            #iiidef
17            if s[l] in vowel:
18                count-=1
19            l+=1
20            if s[r] in vowel:
21                count+=1
22            maxcount=max(maxcount,count)
23        return maxcount