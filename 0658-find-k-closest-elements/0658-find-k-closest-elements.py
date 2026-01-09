class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        # 1️⃣ 找到 x 的插入位置 idx
        idx = bisect.bisect_left(arr, x)  # 返回第一个 >= x 的位置

        # 2️⃣ 初始化左右指针
        left = idx - 1  # 插入点左边
        right = idx     # 插入点右边

        res = []

        # 3️⃣ 扩展左右指针，选出 k 个最接近 x 的元素
        while len(res) < k:
            if left < 0:  # 左边越界，只能从右边取
                res.append(arr[right])
                right += 1
            elif right >= n:  # 右边越界，只能从左边取
                res.append(arr[left])
                left -= 1
            else:
                # x 离左边更近或者相等 → 取左边
                if x - arr[left] <= arr[right] - x:
                    res.append(arr[left])
                    left -= 1
                else:
                    res.append(arr[right])
                    right += 1

        # 4️⃣ 最后返回升序结果
        res.sort()
        return res