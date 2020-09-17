# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/

class Solution:
    # 其实遍历框架基本是一样的，只是什么时候出这个 序 ，才符合我们要的那个遍历顺序
    def preorderTraversal(self, root: TreeNode) -> List[int]:
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
                    order.append(root.val)
                    tmp.right = root
                    root = root.left
                else:
                    tmp.right = None
                    root = root.right
        return order

                
