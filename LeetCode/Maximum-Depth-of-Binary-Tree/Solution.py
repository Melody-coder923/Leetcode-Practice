1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return 0
11        def helper(node):
12            if not node:
13                return 0
14            left=helper(node.left)
15            right=helper(node.right)
16
17            return max(left,right)+1
18        return helper(root)