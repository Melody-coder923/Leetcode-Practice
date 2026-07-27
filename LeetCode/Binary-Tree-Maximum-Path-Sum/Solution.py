1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9        """
10        input: root+binary tree
11        output: path sum(every node only one time+ no need to pass the root)
12
13        孩子告诉父亲： 我单侧最大的path是多少 def -return 孩子告诉父亲
14        父亲决策： 左右孩子加一起比较全局最大值def 内部更新
15        """
16        res=float("-inf")
17
18        def dfs(node):
19            nonlocal res
20            #base case
21            if not node:
22                return 0
23
24            left=max(dfs(node.left),0)
25            right=max(dfs(node.right),0)
26            
27            #postorder-父亲的决策更新
28            res=max(left+right+node.val,res)
29
30            return max(left,right)+node.val
31        
32        #调整体程序返回结果
33        dfs(root)
34        return res