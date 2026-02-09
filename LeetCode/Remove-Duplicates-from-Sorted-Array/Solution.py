1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        #[0,1,1,0,1,2,2,3,3,4]
4        if len(nums) == 0:
5            return 0
6        slow = 0
7        fast = 0
8        while fast < len(nums):
9            if nums[fast] != nums[slow]:
10                slow += 1
11                # 维护 nums[0..slow] 无重复
12                nums[slow] = nums[fast]
13            fast += 1
14        # 数组长度为索引 + 1
15        return slow + 1
16
17
18