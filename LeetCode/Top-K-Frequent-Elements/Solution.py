1from collections import Counter
2class Solution:
3    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
4       count=Counter(nums)
5       sorted_items = sorted(count.items(),key=lambda x: x[1],reverse=True)
6       return [item[0] for item in sorted_items[:k]]
7       