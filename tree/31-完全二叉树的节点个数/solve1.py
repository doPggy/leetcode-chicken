# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode-cn.com/problems/count-complete-tree-nodes/
class Solution:
    def countNodes(self, root: TreeNode) -> int:

        def helper(root):
            if not root:
                return 0
            left_num = helper(root.left)
            right_num = helper(root.right)
            return left_num + right_num + 1
        return helper(root)