1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
9        #base case
10        if not preorder or not inorder:
11            return None
12        
13        root_val= preorder.pop(0) 
14        new_root= TreeNode(root_val)
15        idx= inorder.index(root_val) 
16
17        new_root.left=self.buildTree(preorder,inorder[:idx])
18        new_root.right=self.buildTree(preorder,inorder[idx+1:])
19
20        return new_root