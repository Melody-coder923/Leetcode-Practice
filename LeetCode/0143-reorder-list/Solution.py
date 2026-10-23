# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        # fast/slow - find middle
        slow=head
        fast=head.next
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        #when stop ,slow in middle 
        second_half=slow.next
        slow.next=None
       
    
        # reverse the second half 
        prev=None
        curr=second_half
        while curr:
            nxt_node=curr.next
            curr.next=prev
            prev=curr
            curr=nxt_node

        new_second_half_node=prev

        # loop two linkedlist to build the new one 
        # 1 2 3 None 
        #     P1
        # 4 5
        #.     P2
        # dummy- 1 -4 - 2 -5 -3
        #                      |
        p1=head
        p2=new_second_half_node
        dummy=ListNode(-1)
        curr=dummy
        while p1 and p2:
            curr.next=p1
            curr=curr.next
            p1=p1.next

            curr.next=p2
            curr=curr.next
            p2=p2.next
        
        if p1:
            curr.next=p1
        if p2:
            curr.next=p2
        
        return dummy.next





