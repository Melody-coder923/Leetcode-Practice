class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        #左边：窗口内部已经固定的元素 → 可以直接用

        #右边：窗口右边潜在更优元素 → 必须看窗口外的元素

        # 二分判定函数的目标：找到离 x 最近的长度 k 窗口

        """
        窗口左端点 = mid

        窗口右端点 = mid + k - 1

        窗口外右边的下一个元素 = mid + k → 用来判断是否应该右移窗口
        """

        while left < right:
            mid = (left + right) // 2 
            # 比较窗口左边和右边谁更远离 x
            if x - arr[mid] > arr[mid + k] - x:
                # 说明更靠近 x 的窗口在右边
                left = mid + 1
            else:
                # 当前窗口更靠近 x，或一样近但数值较小，向左缩
                right = mid

        # 最终 left 是最佳窗口起点
        return arr[left:left + k]
