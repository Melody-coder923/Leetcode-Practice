class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if n<=1:
            return nums
        
        # 倒叙遍历
        i=n-2
        flag=True
        while i>=0:               #[3,2,1] nums[i]=2
            if nums[i]<nums[i+1]:  
                break
            else:
                if i==0:
                    flag=False
            i-=1
        if not flag:
            nums.sort()
            return nums

        #此时i是第一个降点
        # 找到第一个比降点大得数字
        if i>=0: 
            j=n-1            
            while j>i:     
                if nums[j]>nums[i]: 
                    break
                j-=1
        #此时得j就是右边第一个比i大的数
        # 交换降点和比他大得数字
        nums[i],nums[j]=nums[j],nums[i]
        #降点原始位置后面升序
        # 千万不要切片, 切片就会生成新的列表对象!!!!!!!!!!!!!!!!!!!!
        nums[i + 1:] = reversed(nums[i + 1:])
        return nums
