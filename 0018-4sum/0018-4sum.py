class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Edge Case:
        n=len(nums)
        if n<4:
            return []

        # step1: 排序 ->方便指导挪动 
        nums.sort()
        res=[]
        # step2: 四个数: 先固定一个外循环 i
        # 2 2 2 2 2 n
        #   i 
        #     j 
        # -5,-2,-1,0,2,2,4,4,4 target=12
        #          i     j l r      
        # 
        for i in range(n-3):     
            if i>0 and nums[i]==nums[i-1]:   
                continue 
            # i 固定后，最小四数和
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break   # 后面的 i 只会更大，直接退出 i 循环

            # i 固定后，最大四数和
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue  # 当前 i 太小，换下一个 i
                
        #step3: 再固定一个, j=i+1
            for j in range(i+1,n-2): 
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
        #step4: while left<right: 朝着target目标, 控制数组大小去移动 
                left=j+1
                right=n-1
                while left<right:
                    total=nums[i]+nums[j]+nums[left]+nums[right]
                    if total==target:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        while left<right and nums[left]==nums[left+1]:
                            left+=1
                        while left<right and nums[right]==nums[right-1]:
                            right-=1
                        left+=1
                        right-=1
                    elif total>target:
                        right-=1
                    
                    else:
                        left+=1
        return res
