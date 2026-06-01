1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
9        def dfs(preorder,inorder):
10            if not inorder:
11                return None
12            root_val = preorder.pop(0)
13            root=TreeNode(root_val)
14            idx=inorder.index(root_val)
15            root.left=dfs(preorder,inorder[:idx])
16            root.right=dfs(preorder,inorder[idx+1:])
17        
18            return root
19        
20        return dfs(preorder,inorder)
21
22
23