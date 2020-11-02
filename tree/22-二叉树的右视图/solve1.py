# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode-cn.com/problems/binary-tree-right-side-view/

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def helper(root):
            if not root:
                return []
            lefts  = helper(root.left)
            rights = helper(root.right)
            left_len  = len(lefts)
            right_len = len(rights)
            if left_len > right_len:
                rights.extend(lefts[right_len:])
            rights.insert(0, root.val)
            return rights
        return helper(root)
