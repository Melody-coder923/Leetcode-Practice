1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
9        val_idx= {val:i for i,val in enumerate(inorder)}
10        self.pre_idx=0
11        def helper(left,right):
12            if left>right:
13                return None
14            val = preorder[self.pre_idx]
15            self.pre_idx+=1
16            
17            root=TreeNode(val)
18            idx=val_idx[val]
19
20            root.left = helper(left, idx - 1)
21            root.right = helper(idx + 1, right)
22
23            return root
24
25        return helper(0,len(inorder)-1)