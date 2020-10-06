# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def post_order(root):
            if not root:
                return
            if root.left:
                root_fathers[root.left.val] = root
            if root.right:
                root_fathers[root.right.val] = root
            post_order(root.left)
            post_order(root.right)
        # 因为数字唯一
        root_fathers = { root.val : None }
        post_order(root)
        has_order = {}
        while p:
            has_order[p.val] = True
            p = root_fathers[p.val]
        while q:
            if has_order.get(q.val):
                return q
            q = root_fathers[q.val] 
