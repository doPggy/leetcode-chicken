# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        def helper(p, q):
            if not p and not q:
                return True
            elif not p and q:
                return False
            elif p and not q:
                return False
            # 这样更好理解
            left_ok  = helper(p.left, q.left)
            right_ok = helper(p.right, q.right)
            return left_ok and right_ok and (p.val == q.val)
        return helper(p, q)

        # 这样更快
        # def helper(p, q):
        #     if not p and not q:
        #         return True
        #     elif not p and q:
        #         return False
        #     elif p and not q:
        #         return False
        #     if p.val == q.val:
        #         left_ok  = helper(p.left, q.left)
        #         right_ok = helper(p.right, q.right)
        #         return left_ok and right_ok
        #     else:
        #         return False