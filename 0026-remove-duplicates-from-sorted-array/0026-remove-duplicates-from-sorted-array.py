class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #[0,1,2,3,4,2,2,3,3,4]
        #         s
        #                   f
        #s 守门
        #f 找不一样
        #找到不一样: s+1 ,替换

        s=0
        for f in range(1,len(nums)):
            if nums[f]!=nums[s]:
                s+=1
                nums[s]=nums[f]

        return s+1
            

