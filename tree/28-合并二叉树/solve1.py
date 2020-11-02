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
            if not t1 and not t2:
                return
            val = 0
            if t1:
                val += t1.val
            if t2:
                val += t2.val
            t1_left     = t1 and t1.left or None
            t2_left     = t2 and t2.left or None
            t1_right    = t1 and t1.right or None
            t2_right    = t2 and t2.right or None
            root        = TreeNode(val)
            root.left   = helper(t1_left, t2_left)
            root.right  = helper(t1_right, t2_right)
            return root
        return helper(t1, t2)