# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode-cn.com/problems/maximum-binary-tree/
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        num_2_index = { val:index for index, val in enumerate(nums) }

        def helper(left, right):
            if left > right:
                return
            max_num       = max(nums[ left:right + 1 ])
            max_num_index = num_2_index[max_num]
            root      = TreeNode(max_num)
            root.left  = helper(left, max_num_index - 1)
            root.right = helper(max_num_index + 1, right)
            return root
        return helper(0, len(nums) - 1)