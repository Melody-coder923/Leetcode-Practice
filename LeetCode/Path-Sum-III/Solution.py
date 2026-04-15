1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def countPathFromNode(self, node, targetSum):
9        if not node:
10            return 0
11        count = 1 if node.val == targetSum else 0
12        count += self.countPathFromNode(node.left, targetSum - node.val)
13        count += self.countPathFromNode(node.right, targetSum - node.val)
14        return count
15
16    def pathSum(self, root, targetSum):
17        if not root:
18            return 0
19        count_from_root = self.countPathFromNode(root, targetSum)
20        count_from_left = self.pathSum(root.left, targetSum)
21        count_from_right = self.pathSum(root.right, targetSum)
22        return count_from_root + count_from_left + count_from_right