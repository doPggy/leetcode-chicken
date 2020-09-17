# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        order = []
        while len(stack) > 0 or root:
            while root:
                stack.append(root)
                root = root.left
            # pop 的位置代表了是哪个序, 中序被访问
            root = stack.pop()
            order.append(root.val)
            root = root.right
        return order