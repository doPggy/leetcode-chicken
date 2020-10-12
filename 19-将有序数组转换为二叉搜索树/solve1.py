# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:            
        # 这个很简单，就是一种递归二分
        def helper(left_idx, right_idx):
            if left_idx > right_idx:
                return
            mid  = int((left_idx + right_idx) / 2)
            root = TreeNode(nums[mid])
            root.left  = helper(left_idx, mid - 1)
            root.right = helper(mid + 1, right_idx)
            return root
        return helper(0, len(nums) - 1)
