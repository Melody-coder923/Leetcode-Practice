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
11        def reverse(node):
12            pre=None
13            cur=node
14            while cur:
15                temp=cur.next
16                cur.next=pre
17                pre=cur
18                cur=temp
19            return pre
20
21        fast=slow=head
22        while fast and fast.next:
23            fast=fast.next.next
24            slow=slow.next
25        p1=head
26        p2=halfhead= reverse(slow.next)
27        slow.next = None
28        
29        while p1 and p2:
30            p1_next = p1.next
31            p2_next = p2.next
32
33            p1.next = p2
34            if not p1_next:
35                break  # l1 完了，直接接上 l2 后续
36            p2.next = p1_next
37
38            p1 = p1_next
39            p2 = p2_next
40
41        return head
42
43
44
45        
46       