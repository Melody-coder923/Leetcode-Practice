class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        slow = 0  # 找正数
        fast = 0  # 找负数
        res = []
        n = len(nums)

        while len(res) < n:
            # 找下一个正数
            while slow < n and nums[slow] < 0:
                slow += 1
            res.append(nums[slow])
            slow += 1

            # 找下一个负数
            while fast < n and nums[fast] > 0:
                fast += 1
            res.append(nums[fast])
            fast += 1

        return res