# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.maxlength=0
        def dfs(node,parent,curlength):
            if not node:
                return 
            if parent and node.val==parent.val+1:
                curlength+=1
            else:
                curlength=1
            self.maxlength=max(self.maxlength,curlength)
            dfs(node.left,node,curlength)
            dfs(node.right,node,curlength)
        dfs(root,None,1)
        return self.maxlength