class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #闭合区间[0,n-2]  因为mid+1不能大于n-1
        #对应开区间(-1,n-1)
        l,r=-1, len(nums)-1
        while l+1<r:
            mid= l+(r-l)//2
            if nums[mid]> nums[mid+1]:#蓝色
                r=mid
            else:
                l=mid
        return r

        """
        定义一种“颜色”：

        🔵 蓝色区：nums[i] > nums[i+1]（在下降）

        ⚪ 白色区：nums[i] < nums[i+1]（在上升）

        峰值一定是：白色 → 蓝色 的分界点
        """