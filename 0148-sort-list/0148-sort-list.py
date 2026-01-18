# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        fast=slow=head
        prev=None
        while fast and fast.next:
            prev=slow
            fast=fast.next.next
            slow=slow.next

        if prev:
            prev.next = None
        
        left_head = head
        right_head = slow

        left=self.sortList(left_head)
        right=self.sortList(right_head)

        return self.mergeList(left,right)



    def mergeList(self,left,right):
        dummy=ListNode(0)
        cur=dummy

        while left and right:
            if left.val<=right.val:
                cur.next=left
                cur=cur.next
                left=left.next
            else:
                cur.next=right
                cur=cur.next
                right=right.next
        
        if left:
            cur.next=left
        if right:
            cur.next=right
        
        return dummy.next

        