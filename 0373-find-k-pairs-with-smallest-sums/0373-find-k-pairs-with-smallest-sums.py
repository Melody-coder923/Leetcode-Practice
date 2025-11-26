import heapq  # 移到类外面

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):  # 加上 self
        if not nums1 or not nums2:
            return []
        
        heap = []
        
        # 初始化：把 nums1 的前 k 个元素与 nums2[0] 配对
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        
        result = []
        while heap and len(result) < k:
            sum_val, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            
            # 扩展：如果 j+1 存在，加入下一个配对
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
        
        return result