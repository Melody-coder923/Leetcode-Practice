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
14            if maxval<=node.val:
15                good=1
16            else:
17                good=0
18            maxval=max(maxval,node.val)
19            left=dfs(node.left,maxval)
20            right=dfs(node.right,maxval)
21
22            return left+right+good
23        return dfs(root,root.val)