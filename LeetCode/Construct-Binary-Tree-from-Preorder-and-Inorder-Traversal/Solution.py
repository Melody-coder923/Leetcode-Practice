1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
9        
10        val_idx= {val:i for i,val in enumerate(inorder)}
11        self.pre_idx=0
12
13        def helper(left,right):
14            if left>right:
15                return None
16            val = preorder[self.pre_idx]
17            self.pre_idx+=1
18            
19            root=TreeNode(val)
20            idx=val_idx[val]
21
22            root.left = helper(left, idx - 1)
23            root.right = helper(idx + 1, right)
24
25            return root
26
27        return helper(0,len(inorder)-1)