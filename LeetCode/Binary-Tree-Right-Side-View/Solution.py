1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
9        if not root:
10            return []
11        res=[]
12        def dfs(node,depth):
13            if not node:
14                return 
15            if len(res)==depth:
16                res.append(node.val)
17            dfs(node.right,depth+1)
18            dfs(node.left,depth+1)
19            return res
20        return dfs(root,0)
21        