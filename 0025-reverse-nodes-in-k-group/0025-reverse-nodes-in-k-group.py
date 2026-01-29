# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Input: Linkedlist , group k  ,consider not multiple of k
        # Output: reverse in group not change val but move the node
        if not head:
            return None
            
        # step helper function: reverse 
        def reverse(node):  
            prev=None
            cur=node 
            while cur:
                temp=cur.next
                cur.next=prev
                prev=cur
                cur=temp
            return prev

        # seperate by group  slow(start)not move -fast(end) move by range
        # for _ in range(k-1): 
        # 1  2   3
        # s  f  nextround
        slow=fast=head
        for _ in range(k-1):
            if not fast.next: 
                return head
            fast=fast.next
        # cut 1,2
        nextround=fast.next
        fast.next=None

           

        # new head=2  2->1 
        newhead=reverse(slow) 
        
        slow.next=self.reverseKGroup(nextround,k)
        return newhead
        

