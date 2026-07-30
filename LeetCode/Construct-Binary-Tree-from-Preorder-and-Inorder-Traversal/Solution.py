1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
9        if not preorder or not inorder:
10            return None
11        pre_idx=0
12        dir={}
13        for i,num in enumerate(inorder):
14            dir[num]=i
15
16        def build(left,right):
17            if left>right:
18                return 
19            nonlocal pre_idx
20            cur_val= preorder[pre_idx]
21            pre_idx += 1
22            node=TreeNode(cur_val)
23            mid=dir[cur_val]
24            node.left=build(left,mid-1)
25            node.right=build(mid+1,right)
26            return node
27        
28        return build(0,len(inorder)-1)
29