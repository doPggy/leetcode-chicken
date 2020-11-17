# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# https://leetcode-cn.com/problems/reverse-linked-list/
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 迭代方式
        # 这里是让当前节点 next 指向前一个节点
        
        pre = None
        q   = head
        while q:
            q_next = q.next
            q.next = pre
            pre    = q
            q      = q_next
        return pre