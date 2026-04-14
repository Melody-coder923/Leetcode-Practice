1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:  
8        if not head or not head.next:
9            return head 
10        odd=head
11        even=head.next
12        connect=even
13        while even and even.next:
14            odd.next=even.next
15            odd=odd.next
16
17            even.next=odd.next
18            even=even.next
19        
20        odd.next=connect
21        return head
22
23
24        # 1     2     3 4 5
25        # odd.  even
26        # 1->3 -> 5
27        #        odd
28        #connect
29        # 2->4-> None
30        #        even
31
32