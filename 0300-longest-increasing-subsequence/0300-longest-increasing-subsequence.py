class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # O(n log(n)) 不能排序sort

        # 二分法才能解决-> 自能用新的数组-> 结果数组,边找位置,边搜集放入

        res=[]
        for num in nums:
            l, r = 0, len(res)
            while l<r:
                mid= l+(r-l)//2
                if num>res[mid]:
                    l=mid+1
                else:
                    r=mid
            #return l
            if l==len(res):
                res.append(num)
            else:
                res[l]=num
        
        return len(res)





        