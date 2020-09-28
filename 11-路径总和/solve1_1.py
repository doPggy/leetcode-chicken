# https://leetcode-cn.com/problems/path-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def helper(root, sum):
            if not root:
                return False
            # 叶节点才计算
            if not root.left and not root.right:
                if root.val == sum:
                    return True
                else:
                    return False

            left_ok  = helper(root.left, sum - root.val)
            right_ok = helper(root.right, sum - root.val)
            return left_ok or right_ok 
        return helper(root, sum)
            