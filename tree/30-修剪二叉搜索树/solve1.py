# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode-cn.com/problems/trim-a-binary-search-tree/
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:

        def trim(root):
            if not root:
                return
            if root.val > high:
                return trim(root.left)
            elif root.val < low:
                return trim(root.right)
            else:
                root.left = trim(root.left)
                root.right = trim(root.right)
            return root
        return trim(root)