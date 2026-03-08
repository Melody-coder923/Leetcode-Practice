1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
8        if not head or left == right:
9            return head
10        dummy=ListNode(-1)
11        dummy.next=head
12        pre = dummy
13        for i in range(left - 1):
14            pre = pre.next
15        start=pre.next
16        end=start
17        for i in range(right - left):
18            end = end.next
19        
20        next_node=end.next
21        end.next=None
22
23        new_head=self.reverse(start)
24        pre.next=new_head
25        start.next=next_node
26
27        return dummy.next
28        
29    def reverse(self,head):
30        pre=None
31        cur=head
32        while cur:
33            nextnode_temp=cur.next
34            cur.next=pre
35            pre=cur
36            cur=nextnode_temp
37        return pre