class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #target: 交叉对比左边和另外一个数组的右边,左<右 
    #且左边数字个数,小于右边数字个数 i+j<= 整个数组一半
    # 1 | 3 
    # 2 | 
    # 单数:取左边最大

    #  1  2 maxleft1|       
    #               |minright  3  4
    # 偶数:取左边最大和右边最小 (2+3)/2

    #      4  5    m =2        12 3  45
    #         i
    #      l   r
    #  1    3  8    n =3
    #          j
    
    # Step1: 移动分割线,实现target
    #以最短的数组为坐标,让num1最短
        m,n=len(nums1),len(nums2) 
        #Edge case:
        if not m and not n:
            return 0.0

        if m>n:
            nums1,nums2=nums2,nums1
        m,n=len(nums1),len(nums2)
        #以最短的数组为坐标
        l,r=0, m 
        while l<=r: # l:0 <= r: 2
            i= (l+r)//2 # nums1左边   0 个数  1      
            j= (m+n+1)//2 -i # nums2左边  3个数  2

            maxleft1=float("-inf") if i==0 else nums1[i-1]
            minright1=float("inf") if i==m else nums1[i]
            maxleft2=float("-inf") if j==0 else nums2[j-1]
            minright2=float("inf") if j==n else nums2[j]

            if maxleft1<=minright2 and maxleft2<=minright1:
                # Step2: 看even,odd个数
                #单数:取左边最大
                if (m+n)%2!=0:
                    return max(maxleft1,maxleft2)
                #偶数:取左边最大和右边最小
                else:
                    return (max(maxleft1,maxleft2)+min(minright1,minright2))/2
                
            elif maxleft1> minright2:
                r=i-1
            else:
                l=i+1
        
                
                # 1 |2 6    m=3
                # l       r=3  
                #                      i=1        
                #    2  3 |  4   n=3      j=2     1  2 2 3 4 6
                #         j 
                

        
        