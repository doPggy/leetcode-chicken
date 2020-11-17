# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# https://leetcode-cn.com/problems/reverse-linked-list/
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # 迭代方式
        q      = head
        r_head = head
        while q:
            q_next = q.next
            if q == head:
                q.next = None
                r_head = q
            else:
                q.next = r_head
                r_head = q
            q = q_next
        return r_head
