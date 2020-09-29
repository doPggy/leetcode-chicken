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
    # 首先想到层序遍历
    # 说实话，这道题要求空间复杂度得是常数级别
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        r         = root
        queue     = [ r, ]
        queue_len = 1
        while queue_len > 0:
            while queue_len > 0:
                r = queue.pop(0)
                if queue_len > 1:
                    r.next = queue[0]
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
                queue_len -= 1
            queue_len = len(queue)
        return root
