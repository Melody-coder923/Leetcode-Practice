1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
8        if not head or left == right:
9            return head
10        # 1. 加虚拟头
11        dummy = ListNode(0)
12        dummy.next = head
13        
14        # 2. 找位置（用最简单的方法）
15        prev = dummy
16        for _ in range(left - 1):
17            prev = prev.next
18        
19        start = prev.next
20        end = start
21        for _ in range(right - left):
22            end = end.next
23        
24        # 3. 保存后续节点
25        next_part = end.next
26        
27        # 4. 断开
28        end.next = None
29        
30        # 5. 反转中间部分（调用标准反转函数）
31        new_head = self.reverse(start)
32        
33        # 6. 重新连接
34        prev.next = new_head
35        start.next = next_part
36        
37        return dummy.next
38
39    def reverse(self, head):
40        # 标准反转，背下来！
41        prev = None
42        curr = head
43        while curr:
44            temp = curr.next
45            curr.next = prev
46            prev = curr
47            curr = temp
48        return prev