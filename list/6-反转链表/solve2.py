# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# https://leetcode-cn.com/problems/reverse-linked-list/
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 递归方式
        def helper(head):
            if not head or not head.next:
                return head 
            t = helper(head.next)
            head.next.next = head
            head.next = None
            return t
        return helper(head)