1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def goodNodes(self, root: TreeNode) -> int:
9        if not root:
10            return 0
11        def dfs(node,maxval):
12            if not node:
13                return 0
14            good=0
15            if node.val>=maxval:
16                good=1
17            maxval=max(maxval,node.val)
18            left=dfs(node.left,maxval)
19            right=dfs(node.right,maxval)
20
21            return left+right+good
22        return dfs(root,root.val)
23