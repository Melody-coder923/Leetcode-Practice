class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        if n <= 1:
            return
        
        i = n - 2
        
        # 1. 找从右往左第一个降点
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i < 0:  # 全递减，如 3 2 1
            nums.reverse()
            return
        
        # 2. 从右找到第一个比 nums[i] 大的
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        
        # 3. 交换
        nums[i], nums[j] = nums[j], nums[i]
        
        # 4. 将 i+1 到末尾反转（保证是最小升序）
        nums[i + 1:] = reversed(nums[i + 1:])
