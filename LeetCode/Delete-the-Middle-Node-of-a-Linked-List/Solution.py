1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if not head or not head.next:
9            return None
10        slow = head
11        fast = head.next.next
12        while fast and fast.next:
13            slow=slow.next
14            fast=fast.next.next
15        if slow.next:
16            slow.next=slow.next.next
17        else:
18            return None
19        return head
20
21
22        