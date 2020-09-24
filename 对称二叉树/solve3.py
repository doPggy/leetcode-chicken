# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode-cn.com/problems/symmetric-tree/
class Solution:
    # 迭代版本一般就需要一个队列来模拟递归的过程，但不是完全相像
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = [ root, root ]
        while len(queue) > 0:
            p = queue.pop(0)
            q = queue.pop(0)
            if p and not q:
                return False
            elif not p and q:
                return False
            elif not p and not q:
                continue
            elif p.val != q.val:
                return False
            queue.append(p.left)
            queue.append(q.right)
            queue.append(p.right)
            queue.append(q.left)
        return True
