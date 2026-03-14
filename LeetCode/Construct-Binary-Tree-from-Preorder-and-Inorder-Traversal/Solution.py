1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
9        if not preorder or not inorder:
10            return 
11        #preoder  root-left -right   -> get root +  build root 
12        root_val=preorder.pop(0)
13        root= TreeNode(root_val)
14        idx= inorder.index(root_val)
15
16        root.left = self.buildTree(preorder,inorder[:idx])
17        root.right= self.buildTree(preorder,inorder[idx+1:])
18        
19        return root