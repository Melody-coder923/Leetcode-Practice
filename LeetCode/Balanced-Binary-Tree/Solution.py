1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        def dfs(node):
10            if not node:
11                return (True,0)
12            leftcondition,leftdepth=dfs(node.left)       
13            rightcondition,rightdepth=dfs(node.right)
14            if leftcondition and rightcondition:
15                if abs(leftdepth - rightdepth) <= 1:
16                    currentcondition = True
17                else:
18                    currentcondition = False
19            else:
20                currentcondition = False
21            currentdepth=max(leftdepth,rightdepth)+1
22            return (currentcondition, currentdepth)
23        return dfs(root)[0]
24           
25        