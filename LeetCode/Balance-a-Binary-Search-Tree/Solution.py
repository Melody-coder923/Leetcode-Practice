class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                inorder(node.left)
                sorted_array.append(node.val)
                inorder(node.right)
        def build(l, r):
            if l <= r:
                mid = (l + r) // 2
                return TreeNode(sorted_array[mid], build(l, mid - 1), build(mid + 1, r))
        sorted_array = []
        inorder(root)
        return build(0, len(sorted_array) - 1)