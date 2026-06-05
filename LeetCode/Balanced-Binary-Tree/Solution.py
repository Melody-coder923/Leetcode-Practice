1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        def dfs(node):
10            if not node:
11                return 0, True 
12            left_height, left_balanced = dfs(node.left)
13            right_height, right_balanced = dfs(node.right)
14            current_balanced = (left_balanced and 
15                              right_balanced and 
16                              abs(left_height - right_height) <= 1)
17            current_height = max(left_height, right_height) + 1
18            return current_height, current_balanced
19        return dfs(root)[1] 