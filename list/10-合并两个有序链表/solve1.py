# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode-cn.com/problems/merge-two-sorted-lists/
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        q1 = l1
        q2 = l2
        head = l1
        q    = l1
        while q1 and q2:
            if q1.val < q2.val:
                q1_next = q1.next
                q.next  = q1
                q       = q.next
                q1      = q1_next
            else:
                q2_next = q2.next
                q.next  = q1
                q       = q.next
                q1      = q1_next