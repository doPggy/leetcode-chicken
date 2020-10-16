# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def flip(root):
            if not root:
                return
            left  = flip(root.left)
            right = flip(root.right)
            root.left = right
            root.right = left
            return root

        def helper(root):
            # if not root:
            #     return
            if root.right:
                right = helper(root.right)
            left = None
            if root.left:
                left = helper(root.left)
            temp = root
            while temp.right:
                temp = temp.right
            temp.right = left
            root.left = None
            return root

        if not root:
            return
        flip(root)
        helper(root)