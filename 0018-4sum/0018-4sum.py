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
        for i in range(n-3):    
            if i>0 and nums[i]==nums[i-1]:   
                continue 
            if nums[0]+nums[1]+nums[2]+nums[3]>target:
                break
            if nums[0]+nums[n-1]+nums[n-2]+nums[n-3]<target:
                continue
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
