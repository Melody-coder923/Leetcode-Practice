# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head
        
        while cur:
            # 如果 cur 有重复，移动到最后一个重复节点
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            # 如果 prev.next 是 cur，说明没有重复，prev 正常往后移
            if prev.next == cur:
                prev = prev.next
            else:
                # prev.next 到 cur 是重复节点，跳过它们
                prev.next = cur.next
            cur = cur.next
        
        return dummy.next