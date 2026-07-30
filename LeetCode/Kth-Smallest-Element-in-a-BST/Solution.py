1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
9        """
10        input: root, k (1-idx)
11        outpyt: val
12        binary search  left-root-right
13        """
14
15        cur=root
16        stack=[]
17        while cur or stack:
18            while cur:
19                stack.append(cur)
20                cur=cur.left
21            cur=stack.pop()
22            k-=1
23            if k==0:
24                return cur.val
25            # 右边
26            cur=cur.right