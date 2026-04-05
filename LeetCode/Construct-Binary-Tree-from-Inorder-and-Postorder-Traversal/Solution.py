1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
9
10        # 哈希表存储中序遍历的值到索引的映射
11        inorder_map = {val: idx for idx, val in enumerate(inorder)}
12        
13        def helper(in_left, in_right, post_left, post_right):
14            # 递归终止条件
15            if in_left > in_right:
16                return None
17            
18            # 后序遍历的最后一个元素是根节点
19            root_val = postorder[post_right]
20            root = TreeNode(root_val)
21            
22            # 在中序遍历中找到根节点的位置
23            root_idx = inorder_map[root_val]
24            
25            # 计算左子树的节点数量
26            left_size = root_idx - in_left
27            
28            # 递归构建左子树和右子树
29            root.left = helper(in_left, root_idx - 1, post_left, post_left + left_size - 1)
30            root.right = helper(root_idx + 1, in_right, post_left + left_size, post_right - 1)
31            
32            return root
33        
34        return helper(0, len(inorder) - 1, 0, len(postorder) - 1)
35