1class Solution:
2    def separateDigits(self, nums: List[int]) -> List[int]:
3        res = []
4        for num in nums:
5            for digit in str(num):
6                res.append(int(digit))
7
8        return res