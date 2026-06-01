1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9        self.maxPath= float('-inf')
10        def dfs(node):
11            if not node:
12                return 0
13            left=max(0,dfs(node.left))
14            right=max(0,dfs(node.right))
15            self.maxPath=max(self.maxPath, left+right+node.val)
16            return node.val+max(left,right)
17        dfs(root)
18        return self.maxPath