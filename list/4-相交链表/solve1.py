# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pa = headA
        pb = headB
        while pa and pb:
            if pa == pb:
                return pa
            pa = pa.next
            pb = pb.next
            if not pa and not pb:
                return
            elif not pa:
                pa = headB
            elif not pb:
                pb = headA
