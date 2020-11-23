# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# https://leetcode-cn.com/problems/palindrome-linked-list/
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        fake_h = ListNode(0)
        fake_h.next = head
        fast = fake_h
        slow = fake_h
        while fast and slow and fast.next:
            # 让 fast 一定在最尾部
            fast = fast.next.next if fast.next.next else fast.next
            slow = slow.next

        # 翻转后半部分链表 
        pre     = None
        reserve = slow.next
        while reserve:
            reserve_next = reserve.next
            reserve.next = pre
            pre          = reserve
            reserve      = reserve_next

        # slow.next = None
        left  = head
        right = fast
        # 为什么只看右边？ 如下示例
        # 1 3 4 3 1
        # 1 3 4 1
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
