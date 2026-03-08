1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
8        dummy=ListNode(-1)
9        dummy.next=head
10        pre = dummy
11        for i in range(left - 1):  
12            pre = pre.next
13        start = pre.next
14        end = start
15        for i in range(right - left):
16            end = end.next
17        next_node = end.next
18        end.next = None
19        pre.next = self.reverse(start)
20        start.next = next_node
21        return dummy.next
22    def reverse(self, head):
23        prev = None
24        curr = head
25        while curr:
26            next_temp = curr.next
27            curr.next = prev
28            prev = curr
29            curr = next_temp
30        return prev