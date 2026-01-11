class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res=[]
        # Step1: 定位x的在arr里面的index
        # 第一个大于等于x的index, 如果 x 比数组中所有元素都大（在右边，超出数组范围)返回len(arr)
        idx= bisect.bisect_left(arr,x) 
        n=len(arr)
        if idx>=n: 
            return arr[n-k:]

        #Step2: 扩大范围
        right=idx
        left=idx-1
    
        while len(res)<k: 
            #base case:
            if left<0:
                res.append(arr[right])
                right+=1
                continue

            if right>=n:
                res.append(arr[left])
                left-=1
                continue
    
            #判断距离谁更近,加谁, left x          right
            if x-arr[left] <= arr[right]-x:
                res.append(arr[left])
                left-=1
            else:
                res.append(arr[right])
                right+=1
        return sorted(res)