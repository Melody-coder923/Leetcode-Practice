class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i, c in enumerate(citations):
            if c >= i + 1:  # 至少 i+1 篇论文引用次数 ≥ i+1
                h = i + 1
            else:
                break
        return h