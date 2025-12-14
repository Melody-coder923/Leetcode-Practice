class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        total=sum(cardPoints)
        if n==k:
            return total
        windowSize = n - k
        windowSum = sum(cardPoints[:windowSize])
        minWindowSum = windowSum

        for i in range(windowSize, n):
            windowSum += cardPoints[i]
            windowSum -= cardPoints[i - windowSize]
            minWindowSum = min(minWindowSum, windowSum)

        return total - minWindowSum