1class Solution:
2    def nextPermutation(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6class Solution:
7    def nextPermutation(self, nums: List[int]) -> None:
8        n = len(nums)
9        if n <= 1:
10            return
11        
12        i = n - 2
13        
14        # 1. 找从右往左第一个降点
15        while i >= 0 and nums[i] >= nums[i + 1]:
16            i -= 1
17        
18        if i < 0:  # 全递减，如 3 2 1
19            nums.reverse()
20            return
21        
22        # 2. 从右找到第一个比 nums[i] 大的
23        j = n - 1
24        while nums[j] <= nums[i]:
25            j -= 1
26        
27        # 3. 交换
28        nums[i], nums[j] = nums[j], nums[i]
29        
30        # 4. 将 i+1 到末尾反转（保证是最小升序）
31        nums[i + 1:] = reversed(nums[i + 1:])
32