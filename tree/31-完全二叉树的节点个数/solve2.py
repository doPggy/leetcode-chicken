# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode-cn.com/problems/count-complete-tree-nodes/
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # 利用完全二叉树的性质
        def helper():