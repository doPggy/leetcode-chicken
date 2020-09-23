# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/
class Solution:
    # 自底向上
    # 相当于后序遍历
    def maxDepth(self, root: TreeNode) -> int:

        def helper(root):
            if not root:
                return 0
            left_depth  = helper(root.left)
            right_depth = helper(root.right)
            # 左右子树的深度，取较大者，再 +1 就是当前节点的深度
            return max(left_depth, right_depth) + 1
        return helper(root)