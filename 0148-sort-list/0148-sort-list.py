# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # divide conquer
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeList(l1,l2):
            dummy=ListNode(0)
            cur=dummy
            while l1 and l2:
                if l1.val<=l2.val:
                    cur.next=l1
                    cur=cur.next
                    l1=l1.next
                else:
                    cur.next=l2
                    cur=cur.next
                    l2=l2.next
            if l1:
                cur.next=l1
            if l2:
                cur.next=l2
            return dummy.next

        #base case
        if not head or not head.next:
            return head
        # divide
        fast=slow=head
        prev=None 
        while fast and fast.next:
            fast=fast.next.next
            prev=slow
            slow=slow.next
        # cut the front and back linkedlist
        prev.next=None

        left=self.sortList(head)
        right=self.sortList(slow)
        return mergeList(left,right)