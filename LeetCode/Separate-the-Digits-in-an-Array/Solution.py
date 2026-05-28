1class Solution:
2    def separateDigits(self, nums: List[int]) -> List[int]:
3        res = []
4        for num in nums:
5            temp = []
6
7            while num > 0:
8                temp.append(num % 10)
9                num //= 10
10
11            res.extend(temp[::-1])
12
13        return res