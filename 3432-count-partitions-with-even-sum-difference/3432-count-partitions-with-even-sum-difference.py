class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        #total 是偶数 → 一定是偶数,total 是奇数 → 一定是奇数,跟 i、left、right 全部无关了
        total = sum(nums)
        n = len(nums)

        if total % 2 == 0:
            return n - 1
        else:
            return 0