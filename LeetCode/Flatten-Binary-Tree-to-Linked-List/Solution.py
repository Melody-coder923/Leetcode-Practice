1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def flatten(self, root: Optional[TreeNode]) -> None:
9        """
10        Do not return anything, modify root in-place instead.
11        """       
12        cur = root
13        while cur:
14            if cur.left:
15                # 找到左子树的最右节点
16                rightmost = cur.left
17                while rightmost.right:
18                    rightmost = rightmost.right
19
20                # 把当前右子树挂到左子树最右节点后面
21                rightmost.right = cur.right
22                # 左子树移到右边，左边置空
23                cur.right = cur.left
24                cur.left = None
25
26            cur = cur.right
27   