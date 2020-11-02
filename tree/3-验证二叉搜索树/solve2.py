# https://leetcode-cn.com/problems/validate-binary-search-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def helper(root, lower, upper):
            if not root:
                return True
            # 类似一种后序遍历
            is_left_ok  = helper(root.left, lower, root.val)
            is_right_ok = helper(root.right, root.val, upper)
            if not is_left_ok or not is_right_ok:
                return False
            if root.val < upper and root.val > lower:
                return True
            else:
                return False
        
        return helper(root, float("-inf"), float("+inf"))