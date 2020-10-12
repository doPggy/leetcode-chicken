# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode-cn.com/problems/diameter-of-binary-tree/
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        def helper(root):
            if not root:
                return 0
            left_h, left_diameter   = helper(root.left)
            right_h, right_diameter = helper(root.right)
            height  = max(left_h, right_h) + 1