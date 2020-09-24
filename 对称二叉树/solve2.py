# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode-cn.com/problems/symmetric-tree/
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def helper(left_tree_root, right_tree_root):
            if not left_tree_root and right_tree_root:
                return
            elif left_tree_root and not right_tree_root:
                return
            elif not left_tree_root and not right_tree_root:
                return True

            if left_tree_root.val != right_tree_root.val:
                return False

            left_ok  = helper(left_tree_root.left, right_tree_root.right)
            right_ok = helper(left_tree_root.right, right_tree_root.left)
            return left_ok and right_ok
        
        return helper(root, root)