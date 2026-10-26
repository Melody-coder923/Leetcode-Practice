# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        left = None
        right = None

        # edge case/base case
        if not root:
            return root

        if root==p or root==q:
            return root
        
        if root.val>p.val and root.val>q.val: 
            left=self.lowestCommonAncestor(root.left,p,q) 
        
        if root.val<p.val and root.val<q.val:
            right=self.lowestCommonAncestor(root.right,p,q) 
        
        if not left and not right:
            return root 
            
        if left and right:
            return root

        if left:
            return left

        if right:
            return right
        
        

        

