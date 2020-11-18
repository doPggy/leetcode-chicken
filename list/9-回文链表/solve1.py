# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# https://leetcode-cn.com/problems/palindrome-linked-list/
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head
        while fast and slow and fast.next:
            fast = fast.next.next
            slow = slow.next
        print(slow)
