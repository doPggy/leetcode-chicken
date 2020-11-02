# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 差点前序写不出来
        if not root:
            return
        stack = [ root ]
        pre   = None
        while len(stack) > 0:
            root = stack.pop()
            # print(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            if not pre:
                pre = root
            else:
                pre.right = root
                pre.left  = None
                pre       = root
            root      = root.left