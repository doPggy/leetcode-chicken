# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [ root, ]
        order = []

        while len(stack) > 0:
            root = stack.pop()
            order.append(root.val)
            # 构造出前序遍历的顺序, 先根，在左，后右
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return order

        