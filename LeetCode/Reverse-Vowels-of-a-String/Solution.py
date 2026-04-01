1class Solution:
2    def reverseVowels(self, s: str) -> str:
3        vowels={'a','e', 'i', 'o','u', 'A','E','I','O','U'}
4        left,right=0,len(s)-1
5        lst=list(s)
6        while left<right:
7            while left<right and lst[left] not in vowels:
8                left+=1
9            #left will stop at vowels
10            while left<right and lst[right] not in vowels:
11                right-=1
12            #right will stop at vowels
13            #reverse only all the vowels
14            lst[left],lst[right]=lst[right],lst[left]
15            left+=1
16            right-=1
17        return "".join(lst)