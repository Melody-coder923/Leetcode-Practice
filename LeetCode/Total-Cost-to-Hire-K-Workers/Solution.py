1import heapq
2from typing import List
3class Solution:
4    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
5        left_heap=[]
6        right_heap=[]
7        total_cost = 0
8        n = len(costs)
9        left_idx = 0
10        right_idx = n - 1
11
12        for _ in range(candidates):
13            if left_idx <= right_idx:
14                heapq.heappush(left_heap, (costs[left_idx], left_idx))
15                left_idx += 1
16            if left_idx <= right_idx:
17                heapq.heappush(right_heap, (costs[right_idx], right_idx))
18                right_idx -= 1
19        for _ in range(k):
20            if not right_heap or (left_heap and left_heap[0] <= right_heap[0]):
21                cost, idx = heapq.heappop(left_heap)
22                total_cost += cost
23                if left_idx <= right_idx:
24                    heapq.heappush(left_heap, (costs[left_idx], left_idx))
25                    left_idx += 1
26            else:
27                cost, idx = heapq.heappop(right_heap)
28                total_cost += cost
29                if left_idx <= right_idx:
30                    heapq.heappush(right_heap, (costs[right_idx], right_idx))
31                    right_idx -= 1
32        return total_cost