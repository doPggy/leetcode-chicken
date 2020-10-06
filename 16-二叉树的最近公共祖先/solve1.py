# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(cur_root):
            if not cur_root:
                return
            is_in_left  = helper(cur_root.left)
            is_in_right = helper(cur_root.right)
            if is_in_right and is_in_left:
                return cur_root
            if cur_root.val == p.val or cur_root.val == q.val:
                return cur_root
            else:
                return is_in_left or is_in_right

        return helper(root)
