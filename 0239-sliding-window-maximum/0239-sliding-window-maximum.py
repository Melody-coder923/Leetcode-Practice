class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        res=[]
        for i in range(len(nums)):

        # 1. 移除队尾比当前元素小的
            while q and nums[q[-1]]<nums[i]:
                q.pop()
        # 2. 当前元素加入队尾
            q.append(i)
        
        # 3. 移除不在窗口内的队首
            if q[0]<= i-k:
                q.popleft()

        # 4. 收集窗口最大值
            if i>=k-1:
                res.append(nums[q[0]])

        return res