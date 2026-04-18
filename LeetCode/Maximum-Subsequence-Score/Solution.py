1import heapq
2from typing import List
3class Solution:
4    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
5        pairs = sorted(zip(nums2, nums1), key=lambda x: x[0], reverse=True)
6        min_heap=[]
7        curr_sum=0
8        max_score=0
9        for min_val, val in pairs:
10            heapq.heappush(min_heap, val)
11            curr_sum += val
12            if len(min_heap) > k:
13                removed = heapq.heappop(min_heap)
14                curr_sum -= removed
15            if len(min_heap) == k:
16                score = curr_sum * min_val
17                max_score = max(max_score, score)
18            
19        return max_score
20                
21                
22            
23            
24            
25
26            
27
28