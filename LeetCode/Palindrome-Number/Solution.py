1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        if x < 0 or (x % 10 == 0 and x != 0):
4            return False
5        list_of_digits = [ digit for digit in str(x)]
6        left=0
7        right=len(list_of_digits)-1
8        while left<right:
9            if list_of_digits[left]!=list_of_digits[right]:
10                return False
11            left+=1
12            right-=1
13        return True