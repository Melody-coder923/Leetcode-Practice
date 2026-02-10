1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        cand = None
4        cnt = 0
5        for x in nums:
6            if cnt == 0:
7                cand = x
8            cnt += 1 if x == cand else -1
9        return cand