# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# https://leetcode-cn.com/problems/linked-list-cycle-ii/
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return
        q = head
        m = {}
        while q:
            if m.get(q):
                return q
            m[q] = True
            q = q.next
        return
