# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# https://leetcode-cn.com/problems/remove-linked-list-elements/
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel      = ListNode(0)
        # 自己造一个为头，真的精妙
        sentinel.next = head

        q   = sentinel.next
        pre = sentinel
        while q:
            if q.val == val:
                pre.next = q.next
            else:
                pre = q
            q   = q.next
        return sentinel.next