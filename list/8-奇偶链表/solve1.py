# Definition for sirgly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode-cn.com/problems/odd-even-linked-list/
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return
        even_tail = head
        q         = head.next
        pre       = head
        cur       = 1
        while q:
            q_next = q.next
            if cur % 2 == 0:
                pre.next       = q.next
                q.next         = even_tail.next
                even_tail.next = q
                even_tail      = q
            else:
                pre = q
            q   = q_next
            cur += 1
        return head