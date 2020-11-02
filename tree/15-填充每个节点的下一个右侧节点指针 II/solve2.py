"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        left_most = root
        head      = root
        while left_most:
            while head:
                # if head.left and head.right:
                #     head.left.next = head.right
                # elif head.left and head.next and head.next.left:
                #     head.left.next = head.next.left
                # elif head.left and head.next and head.next.right:
                #     head.left.next = head.next.right
                # if head.next:
                # head = head.next