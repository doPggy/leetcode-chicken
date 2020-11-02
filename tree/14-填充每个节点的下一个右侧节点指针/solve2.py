"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        r    = root
        left = root
        head = root
        # 不用遍历到最后一层，只需要到 N - 1 层就可以了
        while left.left:
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            left = left.left
            head = left
        return root