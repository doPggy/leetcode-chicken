# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# https://leetcode-cn.com/problems/linked-list-cycle/

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        
        fast = head
        slow = head
        while fast.next:
            fast = fast.next.next
            slow = slow.next
            if not fast:
                return False
            elif fast == slow:
                return True
        return False

