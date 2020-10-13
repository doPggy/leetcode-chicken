# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode-cn.com/problems/diameter-of-binary-tree/
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        # 快接近答案了，但是没有真的理解到，所以差一点
        # 还有就是不愿意用全局
        self.ans = 1
        def helper(root):
            if not root:
                return 0
            left_h   = helper(root.left)
            right_h  = helper(root.right)
            if left_h + right_h + 1 > self.ans:
                self.ans = left_h + right_h + 1
            return max(left_h, right_h) + 1
        helper(root)
        return self.ans - 1 