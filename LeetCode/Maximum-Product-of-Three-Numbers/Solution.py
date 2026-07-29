import heapq
class Solution:
    def maximumProduct(self, array):
        largest = heapq.nlargest(3, array)
        smallest = heapq.nsmallest(2,array)

        return max(largest[0] * largest[1] * largest[2], largest[0] * smallest[0] * smallest[1] )