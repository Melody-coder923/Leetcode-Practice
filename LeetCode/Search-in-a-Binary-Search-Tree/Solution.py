1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
9        # node.val==val: return node / null
10        if not root:
11            return None
12        
13        if root.val==val:
14            return root
15        elif root.val> val:
16            return self.searchBST(root.left,val)
17        else:
18            return self.searchBST(root.right,val)
19        
20        return None
21        