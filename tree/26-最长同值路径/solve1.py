# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode-cn.com/problems/longest-univalue-path/
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:

        # 想法已经往那边靠了，其实也靠对了
        # 但是套完框架后，具体的处理没有想清楚
        # 核心就是怎么计算这个长度 要左右都判断
        #! 忘记了一点，两点路径是不能有环的，我他妈的考虑问题的时候等于把有环的路径考虑进去
        #! 对于当前树来说，向上一层返回只能是最大的路径长度，也就是某一子树，而不是总和
        # 所以只要返回给上一层 这颗树的最大长度 就好
        self.ans = 0
        def helper(root):
            if not root:
                return 0
            left  = helper(root.left)
            right = helper(root.right)

            left_max = right_max = 0
            if root.left and root.left.val == root.val:
                left_max = left + 1
            if root.right and root.right.val == root.val:
                right_max = right + 1
            # 最大路径要算上整颗子树，但对于他的父节点来说，可能只要加上其中一个子树，所以返回的是 right/left_max
            # print(left_max, right_max)
            self.ans = max(self.ans, right_max + left_max)
            return max(right_max, left_max)
        helper(root)
        return self.ans