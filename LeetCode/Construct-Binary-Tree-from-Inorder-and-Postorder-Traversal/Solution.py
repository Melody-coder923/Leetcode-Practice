1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
9        #inorder: left,root,right
10        #               idx
11        #postorder: left,right,root
12        #root ->root_val= postorder.pop()
13        # build TreeNode
14        # idx=inorder.index(root_val)
15        #root.left=inorder[:idx]
16        #root.right=inorder[idx+1:]
17        if not inorder or not postorder:
18            return
19        root_val= postorder.pop()
20        root=TreeNode(root_val)
21        idx= inorder.index(root_val)
22        root.right=self.buildTree(inorder[idx+1:],postorder)
23        root.left=self.buildTree(inorder[:idx],postorder)
24
25        return root