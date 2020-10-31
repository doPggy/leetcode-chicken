# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode-cn.com/problems/convert-bst-to-greater-tree/
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:

        def helper(root, mid_sum):
            if not root:
                return mid_sum
        return root