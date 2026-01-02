class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # 核心是形状识别:找山 上升+top+下降 且长度>=3
        n=len(arr)
        res=0
        i=1
        while i<n:
            upper=0
            lower=0
            #三种状态之一: 平地
            while i<n and arr[i]==arr[i-1]:
                i+=1
            #三种状态之一: 上升
            while i<n and arr[i]>arr[i-1]:
                upper+=1
                i+=1
            #三种状态之一: 下降
            while i<n and arr[i]<arr[i-1]:
                lower+=1
                i+=1  
            if upper > 0 and lower > 0:
                res = max(res, upper + lower + 1)
        return res
           