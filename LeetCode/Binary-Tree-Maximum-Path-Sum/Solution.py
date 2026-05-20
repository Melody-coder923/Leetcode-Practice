1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9        # input: root  node.val<0
10        # output: maxPath
11        # feedback parent: return max(left,right)+node.val
12        # left=max(0,dfs(node.left))
13        # right=max(0,dfs(node.right))
14        # maxPath= max(left+right+node.val, maxPath) global varibale
15        
16        maxPath= float("-inf")
17        def dfs(node):
18            nonlocal maxPath
19            if not node:
20                return 0
21            
22            left=max(dfs(node.left),0)
23            right=max(dfs(node.right),0)
24            maxPath=max(left+right+node.val,maxPath)
25            return max(left,right,0)+node.val
26        dfs(root)
27
28        return maxPath