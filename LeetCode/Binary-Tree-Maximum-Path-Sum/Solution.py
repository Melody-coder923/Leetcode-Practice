1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9        self.ans = float('-inf')  # 全局最大路径和，初始化为负无穷
10        def one_side_max(node):
11            if not node:
12                return 0
13            # 递归计算左右子树的最大贡献值，负数贡献就设为 0
14            left_gain = max(0, one_side_max(node.left))
15            right_gain = max(0, one_side_max(node.right))
16            # 当前路径 = 左 + 根 + 右（当前节点作为路径顶点）
17            current_path_sum = left_gain + right_gain + node.val
18            # 更新全局最大路径和
19            self.ans = max(self.ans, current_path_sum)
20            # 向上传递的最大单边路径（只能走一边）
21            return max(left_gain, right_gain) + node.val
22        one_side_max(root)
23        return self.ans