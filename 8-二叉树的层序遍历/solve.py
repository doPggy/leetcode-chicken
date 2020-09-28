# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue          = [ root, ]
        order          = []
        level          = []
        len_queue      = len(queue)
        while len_queue > 0:
            order.append([])
            while len_queue > 0:
                root = queue.pop(0) # 队列
                order[-1].append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
                len_queue -= 1
            len_queue = len(queue)
        return order