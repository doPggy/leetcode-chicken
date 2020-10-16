# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(root):
            left  = None
            right = None
            if root.left:
                left = helper(root.right)
            if root.right:
                right = helper(root.right)