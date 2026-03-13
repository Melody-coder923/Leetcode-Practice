1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
9        #preorder: 根 左 右
10        #inorder: 左 根 右
11        # preorder-> root 分界
12        #root-> inorder-> left and right 
13        val_idx= {val:i for i,val in enumerate(inorder)}
14        self.pre_idx=0
15        def helper(left,right):
16            if left>right:
17                return None
18            val = preorder[self.pre_idx]
19            self.pre_idx+=1
20            
21            root=TreeNode(val)
22            idx=val_idx[val]
23
24            root.left = helper(left, idx - 1)
25            root.right = helper(idx + 1, right)
26            return root
27
28        return helper(0,len(inorder)-1)
29
30
31
32
33