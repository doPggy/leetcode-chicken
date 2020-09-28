# https://leetcode-cn.com/problems/path-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def helper(root, last_sum, sum):
            if not root:
                return False
            if not root.left and not root.right:
                return last_sum + root.val == sum
            cur_sum  = last_sum + root.val
            left_ok  = helper(root.left, cur_sum, sum)
            right_ok = helper(root.right, cur_sum, sum)
            return left_ok or right_ok

        if not root:
            return False
        return helper(root, 0, sum)