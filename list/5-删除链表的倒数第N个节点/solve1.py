# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast     = head
        slow     = head
        slow_pre = head
        # 一开始设定好距离就行
        for i in range(n - 1):
            if fast.next:
                fast = fast.next
            else:
                break
        # 让指针停在最后一个节点
        while fast.next and slow.next:
            slow_pre = slow
            slow     = slow.next
            fast     = fast.next
        # 如果删除到头结点，那就是要下一个作为头返回
        if slow == head:
            return slow.next
        else:
            slow_pre.next = slow.next
            return head