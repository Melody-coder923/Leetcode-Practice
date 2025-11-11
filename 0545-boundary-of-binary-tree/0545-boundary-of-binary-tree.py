# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root):
        if not root:
            return []

        res = []

        # 判断是否是叶子节点
        def isLeaf(node):
            return not node.left and not node.right

        # 1️⃣ 加入根节点（如果不是叶子）
        if not isLeaf(root):
            res.append(root.val)

        # 2️⃣ 加左边界（不含叶子）
        def addLeftBoundary(node):
            while node:
                if not isLeaf(node):
                    res.append(node.val)
                # 优先往左走，左边界可能“倾斜”
                node = node.left if node.left else node.right

        # 3️⃣ 加所有叶子节点（左→右）
        def addLeaves(node):
            if node:
                if isLeaf(node):
                    res.append(node.val)
                addLeaves(node.left)
                addLeaves(node.right)

        # 4️⃣ 加右边界（不含叶子，反向加入）
        def addRightBoundary(node):
            stack = []
            while node:
                if not isLeaf(node):
                    stack.append(node.val)
                # 优先往右走，右边界可能“倾斜”
                node = node.right if node.right else node.left
            # 逆序加入右边界
            res.extend(reversed(stack))

        # ✨ 按顺序执行
        addLeftBoundary(root.left)
        addLeaves(root)
        addRightBoundary(root.right)

        return res
