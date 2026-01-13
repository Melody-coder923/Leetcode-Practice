class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        1. 提取关键词: 连续（子数组）,最长 ,数量相等
        2. 看到「连续子数组」→ 想“区间”
        3. 区间问题常见工具只有几种：前缀和 与 滑动窗口
        4. 看到「0 和 1 数量相等」→ 出现“平衡关系” (最关键的触发点)
        当你看到这些词时，脑中应该自动亮灯：相等 ,一样多 ,抵消 ,平衡
        👉 这不是在比较位置，而是在比较“数量关系”
        5. 把“相等”改写成“数学式” count(1) == count(0) -> count(1) - count(0) == 0 ⚠️ 这一步是整个解法的“起点”
        6. 能不能让我从左到右扫数组时，用一个变量表示「1 和 0 的数量差」？ 可以 -> 映射 1 → +1  , 0 → -1
         构想[-1, +1, +1, -1, ...]
        7. 原问题被“彻底改写”了: 找一个最长的连续子数组使得 这个子数组的和为 0 👉 问题已经和 0 / 1 无关了
        8. 看到「连续子数组 + 和 = 固定值」→ 前缀和登场
        这是第二个条件反射点： 连续子数组的和 = 前缀和之差 sum(l+1 .. r) = prefix[r] - prefix[l]
        再把和为0带进去 prefix[r] - prefix[l] = 0 ->prefix[r] == prefix[l]
        👉 找的不是区间，而是两个“相同前缀和”的位置
        9.现在问题再次被简化 : 在遍历数组时,找两个下标 l < r, 使得 prefix[l] == prefix[r], 并让 r - l 最大
        10. 怎么快速找到“相同前缀和”？用 HashMap 记录, 因为最长: 同一个前缀和，只能记录「第一次出现的位置」
        11. 如果前缀和在 i 时刻是 0,那说明 (0 .. i) 本身就是合法区间, seen = {0: -1}
        """ 
        prefix = 0
        seen={0:-1}
        max_len=0
        for i in range(len(nums)):
            if nums[i]==0:
               prefix-=1
            if nums[i]==1:
                prefix+=1
            if prefix in seen:
                max_len = max(max_len, i - seen[prefix])
            else:
                seen[prefix]=i
        return max_len
