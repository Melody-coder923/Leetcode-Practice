1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reorderList(self, head: Optional[ListNode]) -> None:
8        """
9        Do not return anything, modify head in-place instead.
10        """
11        if not head:
12            return head
13
14        def reverse(node):
15            prev=None
16            curr=node
17            while curr:
18                nxt=curr.next
19                curr.next=prev
20                prev=curr
21                curr=nxt
22            return prev
23        
24        p1=fast=slow=head
25        while fast and fast.next:
26            fast=fast.next.next
27            slow=slow.next
28        
29        p2=reverse(slow.next)
30        slow.next = None
31
32        while p1 and p2:
33            p1_nxt=p1.next
34            p2_nxt=p2.next
35
36            p1.next = p2
37            if not p1_nxt:
38                break
39            p2.next=p1_nxt
40
41            p1 = p1_nxt
42            p2 = p2_nxt
43            
44        return head
45
46
47        
48
49