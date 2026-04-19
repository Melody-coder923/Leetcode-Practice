1class Solution:
2    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
3        # 从大到小排 min_val
4        pairs = sorted(zip(nums2, nums1), key=lambda x: x[0], reverse=True)
5        min_heap=[]
6        cur_sum=0
7        max_score=0
8        for min_val, num in pairs:
9            heapq.heappush(min_heap,num)
10            cur_sum+=num
11            if len(min_heap) > k:
12                removed = heapq.heappop(min_heap)
13                cur_sum -= removed
14            
15            if len(min_heap)==k:
16                max_score=max(max_score, cur_sum*min_val)
17        return max_score