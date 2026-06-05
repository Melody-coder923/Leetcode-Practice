1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        #no more than 1
10        # father: need to know if left and right are both balanced and their height
11        if not root:
12            return True
13        def dfs(node):
14            if not node:
15                return (True,0)
16            
17            l_balanced, left=dfs(node.left)
18            r_balanced, right=dfs(node.right)
19            if not l_balanced or not r_balanced:
20                return (False,max(left,right))
21            if abs(left-right)>1:
22                return (False,max(left,right))
23            
24            return (True,max(left,right)+1)
25        balanced,height=dfs(root)
26        return balanced
27