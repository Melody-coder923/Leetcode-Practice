# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque([root])
        level=1
        max_sum = float('-inf')
        min_level = 1

        while q:
            size=len(q)
            levelsum=0
            for _ in range(size):
                node = q.popleft()
                levelsum+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if levelsum>max_sum:
                max_sum=levelsum
                min_level=level
                
            level+=1
        
        return min_level