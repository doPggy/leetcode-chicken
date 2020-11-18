# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# https://leetcode-cn.com/problems/remove-linked-list-elements/
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        q   = head
        pre = head
        while q:
            if q.val == val:
                if q == head:
                    head = q.next
                    pre  = q.next
                else:
                    pre.next = q.next
                    # 删除不应该动 pre
                    # pre      = q
            else:
                pre = q
            q = q.next
        return head