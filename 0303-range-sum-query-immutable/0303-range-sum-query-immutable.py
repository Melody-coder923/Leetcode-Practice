class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.prefix_arr = [0] * (n + 1)
        for i in range(n):
            self.prefix_arr[i + 1] = self.prefix_arr[i] + nums[i]
        
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_arr[right + 1] - self.prefix_arr[left]

        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)