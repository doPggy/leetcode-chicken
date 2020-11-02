# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode-cn.com/problems/merge-two-binary-trees/
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        def helper(t1, t2):
            if not t1:
                return t2
            if not t2:
                return t1
            # t1_left     = t1 and t1.left or None
            # t2_left     = t2 and t2.left or None
            # t1_right    = t1 and t1.right or None
            # t2_right    = t2 and t2.right or None
            root        = TreeNode(t1.val + t2.val)
            root.left   = helper(t1.left, t2.left)
            root.right  = helper(t1.right, t2.right)
            return root
        return helper(t1, t2)