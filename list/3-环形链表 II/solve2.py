# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# https://leetcode-cn.com/problems/linked-list-cycle-ii/
class Solution:
    # 这尼玛主要考数学
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return
        fast = head
        slow = head
        while fast.next:
            fast = fast.next.next
            slow = slow.next
            if not fast:
                return
            elif fast == slow:
                q = head
                while q != slow:
                    q    = q.next
                    slow = slow.next
                return q
        return