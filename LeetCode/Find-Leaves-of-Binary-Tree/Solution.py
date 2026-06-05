1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
9        # 搜集叶子节点
10        def collect(node):
11            if not node: 
12                return 
13            if not node.left and not node.right:
14                path.append(node.val)
15                return 
16            collect(node.left)
17            collect(node.right)
18        #删除叶子节点
19        def remove(node):
20            if not node:
21                return None
22            if not node.left and not node.right:
23                return None
24            node.left = remove(node.left) 
25            node.right = remove(node.right)
26            return node
27        
28        if not root:
29            return []
30        res=[]
31        while root:
32            path = []
33            collect(root)
34            res.append(path)
35            root = remove(root)           
36        return res