# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        order = []
        while root:
            if not root.left:
                order.append(root.val)
                root = root.right
            else:
                tmp = root.left
                while tmp.right and tmp.right != root:
                    tmp = tmp.right
                if not tmp.right:
                    tmp.right = root
                    root = root.left
                elif tmp.right == root:
                    tmp.right = None
                    order.append(root.val)
                    root = root.right
        return order

        