# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        order = []
        while root:
            if not root.left:
                root = root.right
            else:
                tmp = root.left
                while tmp.right and tmp.right != root:
                    tmp = tmp.right
                if not tmp.right:
                    tmp.right = root
                    root = root.left
                else:
                    tmp.right = None
                    root = root.right
        return order

                
