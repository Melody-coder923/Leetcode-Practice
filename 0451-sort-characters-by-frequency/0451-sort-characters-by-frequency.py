class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        heap = [(-freq, ch) for ch, freq in counter.items()]
        heapq.heapify(heap)

        res = []
        while heap:
            freq, ch = heapq.heappop(heap)
            res.append(ch * (-freq))
        return ''.join(res)