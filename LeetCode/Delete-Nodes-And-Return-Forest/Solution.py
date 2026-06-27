1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
9        to_delete=set(to_delete)
10        res=[]
11        def dfs(node):
12            if not node:
13                return None
14
15            node.left = dfs(node.left)
16            node.right = dfs(node.right)
17
18            if node.val in to_delete:
19                if node.left:
20                    res.append(node.left)
21                if node.right:
22                    res.append(node.right)
23                return None
24
25            return node
26
27        root = dfs(root)
28
29        if root:
30            res.append(root)
31
32        return res
33
34