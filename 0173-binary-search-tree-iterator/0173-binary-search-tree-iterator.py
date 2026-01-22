# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    #Input: In-order left-root-right  + BST

    def __init__(self, root: Optional[TreeNode]):
        # none-> smallest number -> sort(in-order)
        # container
        self.stack =[]
        self.push(root)
        #The pointer should be initialized to a non-existent number smaller than any element in the BST.
    
    def push(self,node):
        # left root right  
        cur=node
        while cur:
            self.stack.append(cur)
            cur=cur.left
        # left finish 

    def next(self) -> int:
        while self.stack:
            node=self.stack.pop()
            if node.right:
                self.push(node.right)
            return node.val
        
    def hasNext(self) -> bool:
        return bool(self.stack)
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()