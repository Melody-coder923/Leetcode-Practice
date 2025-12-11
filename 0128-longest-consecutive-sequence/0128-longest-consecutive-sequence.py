class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        check = set(nums)
        longest = 0

        for num in check:
            if num - 1 not in check: 
                cur = num
                length = 1

                while cur + 1 in check:
                    cur += 1
                    length += 1

                longest = max(longest, length)

        return longest