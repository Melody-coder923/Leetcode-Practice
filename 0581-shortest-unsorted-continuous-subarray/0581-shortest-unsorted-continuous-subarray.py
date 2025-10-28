class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        newnums = sorted(nums)
        start, end = len(nums), 0
        for i in range(len(nums)):
            if nums[i] != newnums[i]:
                start = min(start, i)
                end = max(end, i)
        return end - start + 1 if end > start else 0