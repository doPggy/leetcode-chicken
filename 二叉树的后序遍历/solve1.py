# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [ root, ]
        order = []
        pre   = None
        while len(stack) > 0 or root:
            while root:
                if root.left:
                    stack.append(root.left)
                if root.right:
                    stack.append(root.right)
                # 遍历
                if root.right and not root.left:
                    root = root.right
                else:
                    root = root.left
            # 一定是叶子节点
            root = stack.pop()
            # print(pre.val)
            # print(root.val)
            order.append(root.val)
            if root.right and root.right == pre:
                root = stack.pop()
            pre  = root
            root = root.right
        return order

