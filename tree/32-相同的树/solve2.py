# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        queue_p = [ p ]
        queue_q = [ q ]

        while len(queue_p) > 0 and len(queue_q) > 0:
            p = queue_p.pop(0)
            q = queue_q.pop(0)
            if not p and not q:
                continue
            if not p and q:
                return False
            elif p and not q:
                return False
            if p.val == q.val:
                queue_p.append(p.left)
                queue_p.append(p.right)
                queue_q.append(q.left)
                queue_q.append(q.right)
            else:
                return False
        return True