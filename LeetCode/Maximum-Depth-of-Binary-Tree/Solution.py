1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        #base case
10        if not root:
11            return 0
12        
13        left=self.maxDepth(root.left)
14        right=self.maxDepth(root.right)
15
16        return max(left,right)+1