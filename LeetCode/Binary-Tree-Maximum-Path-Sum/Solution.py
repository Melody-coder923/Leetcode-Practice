1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9        res = float("-inf")
10        def dfs(node):
11            nonlocal res
12            if not node:
13                return 0
14            left = max(dfs(node.left), 0)
15            right = max(dfs(node.right), 0)
16            
17            res=max(res,left+right+node.val)
18        
19            return max(left,right)+node.val #告诉爸爸
20        dfs(root)
21        return res