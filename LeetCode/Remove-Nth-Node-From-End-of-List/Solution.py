1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        # fast停留到最后的时候，slow要停留在想要删除的前一个
9        # fast和slow之间距离=n
10        if not head:
11            return head
12        dummy = ListNode(0)
13        dummy.next = head
14
15        fast = slow = dummy
16        for _ in range(n+1):
17            fast=fast.next
18    
19        while fast:
20            fast=fast.next
21            slow=slow.next
22        # fast 在最后， slow 在想要删除的前一个
23        slow.next=slow.next.next
24    
25        return dummy.next